import os
import json
from PIL import Image

# 定义路径
yolo_dataset_path = "/Users/qingrui/Desktop/COCO_DATASET"
images_path = os.path.join(yolo_dataset_path, "images")
labels_path = os.path.join(yolo_dataset_path, "labels")

# 定义类别名称
class_names = ["damage_require_restoration", "damage_not_require_restoration"]

# 创建 COCO 格式的数据结构
coco_data = {
    "info": {
        "description": "YOLO to COCO conversion",
        "version": "1.0",
        "year": 2024,
        "contributor": "",
        "date_created": ""
    },
    "licenses": [],
    "images": [],
    "annotations": [],
    "categories": []
}

# 添加类别
for i, class_name in enumerate(class_names):
    coco_data["categories"].append({
        "id": i,
        "name": class_name,
        "supercategory": ""
    })

# 处理图像和标签
annotation_id = 0
for image_id, image_filename in enumerate(os.listdir(images_path)):
    if not image_filename.endswith(('.jpg', '.jpeg', '.tif')):
        continue

    image_path = os.path.join(images_path, image_filename)
    label_path = os.path.join(labels_path, os.path.splitext(image_filename)[0] + '.txt')

    # 读取图像以获取宽高
    with Image.open(image_path) as img:
        width, height = img.size

    # 添加图像信息到 COCO 数据结构
    coco_data["images"].append({
        "id": image_id,
        "file_name": image_filename,
        "width": width,
        "height": height
    })

    # 处理标签文件
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

                # 添加标注信息到 COCO 数据结构
                coco_data["annotations"].append({
                    "id": annotation_id,
                    "image_id": image_id,
                    "category_id": int(class_id),
                    "bbox": [x_min, y_min, bbox_width, bbox_height],
                    "area": bbox_width * bbox_height,
                    "iscrowd": 0
                })
                annotation_id += 1

# 保存为 COCO 格式的 JSON 文件
with open(os.path.join(yolo_dataset_path, "annotations.json"), "w") as f:
    json.dump(coco_data, f, indent=4)

print("YOLO 数据集已成功转换为 COCO 格式")

