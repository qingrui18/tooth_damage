import os
import random
import shutil

def split_dataset_with_labels(source_image_folder, source_label_folder, train_image_folder, train_label_folder, test_image_folder, test_label_folder, split_ratio=0.8):
    # 获取源图像文件夹中所有的图像文件名
    image_files = [f for f in os.listdir(source_image_folder) if not f.startswith('.')]
    random.shuffle(image_files)  # 随机打乱文件顺序

    # 计算分割点
    split_point = int(len(image_files) * split_ratio)

    # 分割文件列表
    train_files = image_files[:split_point]
    test_files = image_files[split_point:]

    # 创建目标文件夹（如果不存在）
    os.makedirs(train_image_folder, exist_ok=True)
    os.makedirs(train_label_folder, exist_ok=True)
    os.makedirs(test_image_folder, exist_ok=True)
    os.makedirs(test_label_folder, exist_ok=True)

    # 复制文件到训练集和测试集文件夹
    for file in train_files:
        src_image_path = os.path.join(source_image_folder, file)
        src_label_path = os.path.join(source_label_folder, os.path.splitext(file)[0] + '.txt')

        dst_image_path = os.path.join(train_image_folder, file)
        dst_label_path = os.path.join(train_label_folder, os.path.splitext(file)[0] + '.txt')

        shutil.copy2(src_image_path, dst_image_path)
        print(f"Copied {file} to {train_image_folder}")

        if os.path.exists(src_label_path):
            shutil.copy2(src_label_path, dst_label_path)
            print(f"Copied {os.path.splitext(file)[0] + '.txt'} to {train_label_folder}")

    for file in test_files:
        src_image_path = os.path.join(source_image_folder, file)
        src_label_path = os.path.join(source_label_folder, os.path.splitext(file)[0] + '.txt')

        dst_image_path = os.path.join(test_image_folder, file)
        dst_label_path = os.path.join(test_label_folder, os.path.splitext(file)[0] + '.txt')

        shutil.copy2(src_image_path, dst_image_path)
        print(f"Copied {file} to {test_image_folder}")

        if os.path.exists(src_label_path):
            shutil.copy2(src_label_path, dst_label_path)
            print(f"Copied {os.path.splitext(file)[0] + '.txt'} to {test_label_folder}")

# 指定源文件夹和目标文件夹路径
source_image_folder = "/Users/qingrui/Desktop/TOOTH_DAMAGE_DATASET/no_damage/images_as_class_tif"
source_label_folder = "/Users/qingrui/Desktop/TOOTH_DAMAGE_DATASET/no_damage/labels_as_class"
train_image_folder = "/Users/qingrui/Desktop/YOLOV8/DATASET/FULL_AREA_3_CLASS/images/train"
train_label_folder = "/Users/qingrui/Desktop/YOLOV8/DATASET/FULL_AREA_3_CLASS/labels/train"
test_image_folder = "/Users/qingrui/Desktop/YOLOV8/DATASET/FULL_AREA_3_CLASS/images/val"
test_label_folder = "/Users/qingrui/Desktop/YOLOV8/DATASET/FULL_AREA_3_CLASS/labels/val"

# 分割比例（如 0.8 表示 80% 训练集，20% 测试集）
split_ratio = 0.8

split_dataset_with_labels(source_image_folder, source_label_folder, train_image_folder, train_label_folder, test_image_folder, test_label_folder, split_ratio)

