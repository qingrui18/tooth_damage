import os
import json


# 定义数据集路径
train_annotations_path = "/Users/qingrui/Desktop/COCO_DATASET/train/annotations.json"
train_images_path = "Users/qingrui/Desktop/COCO_DATASET/train/images"
val_annotations_path = "/Users/qingrui/Desktop/COCO_DATASET/train/annotations.json"
val_images_path = "Users/qingrui/Desktop/COCO_DATASET/val/images"


# 函数来检查和修复图像尺寸
def check_and_fix_image_sizes(annotations_path, images_path):
    with open(annotations_path) as f:
        coco_data = json.load(f)

    for image_info in coco_data["images"]:
        image_path = os.path.join(images_path, image_info["file_name"])
        if os.path.exists(image_path):
            with Image.open(image_path) as img:
                width, height = img.size
                if width != image_info["width"] or height != image_info["height"]:
                    print(f"Image {image_info['file_name']} has mismatched size: "
                          f"actual ({width}, {height}), expected ({image_info['width']}, {image_info['height']})")
                    # 更新标注文件中的尺寸信息
                    image_info["width"] = width
                    image_info["height"] = height

    with open(annotations_path, "w") as f:
        json.dump(coco_data, f)


# 检查和修复训练和验证集的图像尺寸
check_and_fix_image_sizes(train_annotations_path, train_images_path)
check_and_fix_image_sizes(val_annotations_path, val_images_path)