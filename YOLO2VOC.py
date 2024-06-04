import os
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
from PIL import Image

# 定义路径
yolo_dataset_path = "/Users/qingrui/Desktop/VOC_DATASET/VOC_FULL_CV"
images_path = os.path.join(yolo_dataset_path, "images")
labels_path = os.path.join(yolo_dataset_path, "labels")
voc_output_path = os.path.join(yolo_dataset_path, "VOC")

# 确保输出目录存在
if not os.path.exists(voc_output_path):
    os.makedirs(voc_output_path)

# 定义类别名称
class_names = ["damage_require_restoration", "damage_not_require_restoration","no_damage"]


# 创建 VOC 格式的 XML 文件
def create_voc_xml(image_filename, image_size, annotations, output_dir):
    annotation = ET.Element("annotation")

    folder = ET.SubElement(annotation, "folder")
    folder.text = os.path.basename(output_dir)

    filename = ET.SubElement(annotation, "filename")
    filename.text = image_filename

    size = ET.SubElement(annotation, "size")
    width = ET.SubElement(size, "width")
    height = ET.SubElement(size, "height")
    depth = ET.SubElement(size, "depth")
    width.text = str(image_size[0])
    height.text = str(image_size[1])
    depth.text = "3"  # 假设图像为 RGB 三通道

    for ann in annotations:
        obj = ET.SubElement(annotation, "object")
        name = ET.SubElement(obj, "name")
        name.text = class_names[ann["class_id"]]
        pose = ET.SubElement(obj, "pose")
        pose.text = "Unspecified"
        truncated = ET.SubElement(obj, "truncated")
        truncated.text = "0"
        difficult = ET.SubElement(obj, "difficult")
        difficult.text = "0"

        bndbox = ET.SubElement(obj, "bndbox")
        xmin = ET.SubElement(bndbox, "xmin")
        ymin = ET.SubElement(bndbox, "ymin")
        xmax = ET.SubElement(bndbox, "xmax")
        ymax = ET.SubElement(bndbox, "ymax")

        xmin.text = str(int(ann["bbox"][0]))
        ymin.text = str(int(ann["bbox"][1]))
        xmax.text = str(int(ann["bbox"][2]))
        ymax.text = str(int(ann["bbox"][3]))

    xml_str = ET.tostring(annotation)
    parsed_str = parseString(xml_str).toprettyxml(indent="    ")

    with open(os.path.join(output_dir, os.path.splitext(image_filename)[0] + ".xml"), "w") as f:
        f.write(parsed_str)


# 处理图像和标签
for image_filename in os.listdir(images_path):
    if not image_filename.endswith(('.jpg', '.tif', '.png')):
        continue

    image_path = os.path.join(images_path, image_filename)
    label_path = os.path.join(labels_path, os.path.splitext(image_filename)[0] + '.txt')

    # 读取图像以获取宽高
    with Image.open(image_path) as img:
        width, height = img.size

    # 读取标签文件
    annotations = []
    if os.path.exists(label_path):
        with open(label_path) as f:
            for line in f:
                class_id, x_center, y_center, bbox_width, bbox_height = map(float, line.strip().split())
                x_center *= width
                y_center *= height
                bbox_width *= width
                bbox_height *= height
                x_min = x_center - bbox_width / 2
                y_min = y_center - bbox_height / 2
                x_max = x_center + bbox_width / 2
                y_max = y_center + bbox_height / 2

                annotations.append({
                    "class_id": int(class_id),
                    "bbox": [x_min, y_min, x_max, y_max]
                })

    # 创建 VOC XML 文件
    create_voc_xml(image_filename, (width, height), annotations, voc_output_path)

print("YOLO 数据集已成功转换为 VOC 格式")
