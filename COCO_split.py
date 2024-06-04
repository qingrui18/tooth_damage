import os
import json
import random
import shutil


# 定义数据集路径
dataset_path = "/Users/qingrui/Desktop/COCO_DATASET"
annotations_path = os.path.join(dataset_path, "annotations.json")
images_path = os.path.join(dataset_path, "images")

# 读取COCO格式的标注文件
with open(annotations_path) as f:
    coco_data = json.load(f)

# 将数据集分为训练集和验证集
random.seed(42)
image_ids = list(set([ann["image_id"] for ann in coco_data["annotations"]]))
random.shuffle(image_ids)
split_idx = int(0.8 * len(image_ids))
train_ids = set(image_ids[:split_idx])
val_ids = set(image_ids[split_idx:])

train_images = []
val_images = []
train_annotations = []
val_annotations = []

for img in coco_data["images"]:
    if img["id"] in train_ids:
        train_images.append(img)
    else:
        val_images.append(img)

for ann in coco_data["annotations"]:
    if ann["image_id"] in train_ids:
        train_annotations.append(ann)
    else:
        val_annotations.append(ann)

train_coco = {
    "info": coco_data.get("info", {}),
    "licenses": coco_data.get("licenses", []),
    "images": train_images,
    "annotations": train_annotations,
    "categories": coco_data["categories"]
}

val_coco = {
    "info": coco_data.get("info", {}),
    "licenses": coco_data.get("licenses", []),
    "images": val_images,
    "annotations": val_annotations,
    "categories": coco_data["categories"]
}

# 创建训练和验证集目录
train_dir = os.path.join(dataset_path, "train")
val_dir = os.path.join(dataset_path, "val")

if not os.path.exists(train_dir):
    os.makedirs(train_dir)
    os.makedirs(os.path.join(train_dir, "images"))

if not os.path.exists(val_dir):
    os.makedirs(val_dir)
    os.makedirs(os.path.join(val_dir, "images"))

# 保存新的标注文件
with open(os.path.join(train_dir, "annotations.json"), "w") as f:
    json.dump(train_coco, f)
with open(os.path.join(val_dir, "annotations.json"), "w") as f:
    json.dump(val_coco, f)

# 复制图像文件到对应目录
for img in train_images:
    shutil.copy(os.path.join(images_path, img["file_name"]), os.path.join(train_dir, "images"))
for img in val_images:
    shutil.copy(os.path.join(images_path, img["file_name"]), os.path.join(val_dir, "images"))

