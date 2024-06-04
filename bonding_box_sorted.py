import os
import xml.etree.ElementTree as ET
import numpy as np


def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    boxes = []
    for obj in root.findall("object"):
        bbox = obj.find("bndbox")
        xmin = int(bbox.find("xmin").text)
        ymin = int(bbox.find("ymin").text)
        xmax = int(bbox.find("xmax").text)
        ymax = int(bbox.find("ymax").text)
        width = xmax - xmin
        height = ymax - ymin
        area = width * height
        boxes.append(area)
    return boxes


def classify_boxes(box_areas):
    box_areas = np.array(box_areas)
    # 按面积排序
    sorted_areas = np.sort(box_areas)

    # 计算每个类别的边界
    total_boxes = len(sorted_areas)
    small_threshold = sorted_areas[int(total_boxes / 3)]
    medium_threshold = sorted_areas[int(2 * total_boxes / 3)]

    small_boxes = box_areas[box_areas <= small_threshold]
    medium_boxes = box_areas[(box_areas > small_threshold) & (box_areas <= medium_threshold)]
    large_boxes = box_areas[box_areas > medium_threshold]

    # 打印阈值及其对应的分辨率
    small_res = int(np.sqrt(small_threshold))
    medium_res = int(np.sqrt(medium_threshold))

    print(f"Small threshold: {small_threshold} (approx. {small_res}x{small_res})")
    print(f"Medium threshold: {medium_threshold} (approx. {medium_res}x{medium_res})")

    return small_boxes, medium_boxes, large_boxes


def main(xml_folder):
    all_boxes = []
    for xml_file in os.listdir(xml_folder):
        if xml_file.endswith('.xml'):
            file_path = os.path.join(xml_folder, xml_file)
            boxes = parse_xml(file_path)
            all_boxes.extend(boxes)

    small_boxes, medium_boxes, large_boxes = classify_boxes(all_boxes)

    print(f"Total boxes: {len(all_boxes)}")
    print(f"Small boxes: {len(small_boxes)}")
    print(f"Medium boxes: {len(medium_boxes)}")
    print(f"Large boxes: {len(large_boxes)}")


if __name__ == "__main__":
    xml_folder = '/Users/qingrui/Desktop/FASTER_RCNN/DATASET/Annotations'  # 替换为你的 XML 文件所在文件夹路径
    main(xml_folder)

