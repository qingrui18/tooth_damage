import os
from PIL import Image

def convert_jpg_to_tif(source_folder, output_folder):
    # 如果输出文件夹不存在，则创建它
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(source_folder):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            # 构建完整的文件路径
            jpg_path = os.path.join(source_folder, filename)
            # 构建输出文件的路径
            tif_filename = os.path.splitext(filename)[0] + ".tif"
            tif_path = os.path.join(output_folder, tif_filename)

            # 打开 JPG 文件并保存为 TIFF 文件
            with Image.open(jpg_path) as img:
                img.save(tif_path, "TIFF")
            print(f"Converted {jpg_path} to {tif_path}")


# 指定输入和输出文件夹路径
source_folder = "/Users/qingrui/Desktop/TOOTH_DAMAGE_DATASET/no_damage/images_as_class"
output_folder = "/Users/qingrui/Desktop/TOOTH_DAMAGE_DATASET/no_damage/images_as_class_tif"

convert_jpg_to_tif(source_folder, output_folder)
