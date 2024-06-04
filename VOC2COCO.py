import os
import json
import xml.etree.ElementTree as ET
from collections import defaultdict
from PIL import Image


def convert_voc_to_coco(voc_dir, output_file):
    categories = []
    category_set = dict()
    image_set = set()
    image_id = 1
    annotation_id = 1
    coco = dict()
    coco['images'] = []
    coco['type'] = 'instances'
    coco['annotations'] = []
    coco['categories'] = []

    # Collect all categories
    for xml_file in os.listdir(voc_dir):
        if not xml_file.endswith('.xml'):
            continue
        tree = ET.parse(os.path.join(voc_dir, xml_file))
        root = tree.getroot()
        for obj in root.findall('object'):
            category = obj.find('name').text
            if category not in category_set:
                new_id = len(category_set) + 1
                category_set[category] = new_id
                categories.append({
                    'supercategory': 'none',
                    'id': new_id,
                    'name': category
                })

    coco['categories'] = categories

    # Collect all images and annotations
    for xml_file in os.listdir(voc_dir):
        if not xml_file.endswith('.xml'):
            continue
        tree = ET.parse(os.path.join(voc_dir, xml_file))
        root = tree.getroot()
        filename = root.find('filename').text
        if filename in image_set:
            continue
        image_set.add(filename)
        img_path = os.path.join(voc_dir, filename)
        size = root.find('size')
        width = int(size.find('width').text)
        height = int(size.find('height').text)
        image = {
            'file_name': filename,
            'height': height,
            'width': width,
            'id': image_id
        }
        coco['images'].append(image)

        for obj in root.findall('object'):
            category = obj.find('name').text
            category_id = category_set[category]
            bndbox = obj.find('bndbox')
            xmin = int(bndbox.find('xmin').text)
            ymin = int(bndbox.find('ymin').text)
            xmax = int(bndbox.find('xmax').text)
            ymax = int(bndbox.find('ymax').text)
            o_width = abs(xmax - xmin)
            o_height = abs(ymax - ymin)
            ann = {
                'area': o_width * o_height,
                'iscrowd': 0,
                'image_id': image_id,
                'bbox': [xmin, ymin, o_width, o_height],
                'category_id': category_id,
                'id': annotation_id,
                'ignore': 0,
                'segmentation': []
            }
            coco['annotations'].append(ann)
            annotation_id += 1

        image_id += 1

    with open(output_file, 'w') as outfile:
        json.dump(coco, outfile, indent=4)


# 使用示例
voc_dir = '/Users/qingrui/Desktop/FASTER_RCNN/DATASET/FULL_SCALE/Annotations'
output_file = '/Users/qingrui/Desktop/test/coco_annotations.json'
convert_voc_to_coco(voc_dir, output_file)

