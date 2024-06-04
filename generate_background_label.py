import os
import xml.etree.ElementTree as ET


def create_voc_annotation(image_path, annotation_path):
    # 获取图像文件名和路径
    image_name = os.path.basename(image_path)
    annotation_name = image_name.replace(".jpg", ".xml").replace(".png", ".xml").replace(".jpeg", ".xml").replace(
        ".tif", ".xml")

    # 创建XML结构
    annotation = ET.Element("annotation")

    folder = ET.SubElement(annotation, "folder").text = os.path.basename(os.path.dirname(image_path))
    filename = ET.SubElement(annotation, "filename").text = image_name
    path = ET.SubElement(annotation, "path").text = image_path

    source = ET.SubElement(annotation, "source")
    database = ET.SubElement(source, "database").text = "Unknown"

    size = ET.SubElement(annotation, "size")
    width = ET.SubElement(size, "width").text = str(512)  # 你可以使用实际的图像宽度
    height = ET.SubElement(size, "height").text = str(512)  # 你可以使用实际的图像高度
    depth = ET.SubElement(size, "depth").text = str(3)  # 你可以使用实际的图像通道数

    segmented = ET.SubElement(annotation, "segmented").text = "0"

    # 转换为字符串并保存到文件
    tree = ET.ElementTree(annotation)
    tree.write(os.path.join(annotation_path, annotation_name))


def generate_annotations(image_dir, annotation_dir):
    if not os.path.exists(annotation_dir):
        os.makedirs(annotation_dir)

    for image_filename in os.listdir(image_dir):
        if image_filename.endswith((".jpg", ".jpeg", ".png", ".tif")):
            image_path = os.path.join(image_dir, image_filename)
            create_voc_annotation(image_path, annotation_dir)
            print(f"Annotation for {image_filename} created.")


# 指定图像目录和标注文件目录
image_directory = "/Users/qingrui/Desktop/bk_crop"
annotation_directory = "/Users/qingrui/Desktop/bk_ann"

# 生成标注文件
generate_annotations(image_directory, annotation_directory)
