import os
import xml.etree.ElementTree as ET
from PIL import Image


def yolo_to_voc(yolo_file, img_dir, voc_output_dir, class_names):
    with open(yolo_file, 'r') as file:
        lines = file.readlines()

    img_name = os.path.splitext(os.path.basename(yolo_file))[0] + '.tif'
    img_path = os.path.join(img_dir, img_name)
    img = Image.open(img_path)
    width, height = img.size

    annotation = ET.Element('annotation')
    ET.SubElement(annotation, 'folder').text = os.path.basename(img_dir)
    ET.SubElement(annotation, 'filename').text = img_name
    ET.SubElement(annotation, 'path').text = img_path

    source = ET.SubElement(annotation, 'source')
    ET.SubElement(source, 'database').text = 'Unknown'

    size = ET.SubElement(annotation, 'size')
    ET.SubElement(size, 'width').text = str(width)
    ET.SubElement(size, 'height').text = str(height)
    ET.SubElement(size, 'depth').text = '3'

    ET.SubElement(annotation, 'segmented').text = '0'

    for line in lines:
        class_id, x_center, y_center, w, h = map(float, line.strip().split())
        class_name = class_names[int(class_id)]

        xmin = int((x_center - w / 2) * width)
        ymin = int((y_center - h / 2) * height)
        xmax = int((x_center + w / 2) * width)
        ymax = int((y_center + h / 2) * height)

        obj = ET.SubElement(annotation, 'object')
        ET.SubElement(obj, 'name').text = class_name
        ET.SubElement(obj, 'pose').text = 'Unspecified'
        ET.SubElement(obj, 'truncated').text = '0'
        ET.SubElement(obj, 'difficult').text = '0'
        bbox = ET.SubElement(obj, 'bndbox')
        ET.SubElement(bbox, 'xmin').text = str(xmin)
        ET.SubElement(bbox, 'ymin').text = str(ymin)
        ET.SubElement(bbox, 'xmax').text = str(xmax)
        ET.SubElement(bbox, 'ymax').text = str(ymax)

    tree = ET.ElementTree(annotation)
    voc_output_path = os.path.join(voc_output_dir, os.path.splitext(os.path.basename(yolo_file))[0] + '.xml')
    tree.write(voc_output_path)


def batch_convert_yolo_to_voc(yolo_dir, img_dir, voc_output_dir, class_names):
    os.makedirs(voc_output_dir, exist_ok=True)

    for yolo_file in os.listdir(yolo_dir):
        if yolo_file.endswith('.txt'):
            yolo_file_path = os.path.join(yolo_dir, yolo_file)
            yolo_to_voc(yolo_file_path, img_dir, voc_output_dir, class_names)
            print(f"Converted {yolo_file} to VOC format.")


if __name__ == "__main__":
    yolo_dir = '/Users/qingrui/Desktop/TOOTH_DAMAGE_DATASET/damage_require_restoration/annotations_damages'
    img_dir = '/Users/qingrui/Desktop/TOOTH_DAMAGE_DATASET/damage_require_restoration/images'
    voc_output_dir = '/Users/qingrui/Desktop/test'
    class_names = ['damage_require_restoration', 'damage_not_require_restoration']  # Replace with your actual class names

    batch_convert_yolo_to_voc(yolo_dir, img_dir, voc_output_dir, class_names)

