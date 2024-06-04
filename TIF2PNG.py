import os
from PIL import Image


def convert_tif_to_png(input_folder, output_folder):
    # 如果输出文件夹不存在，则创建它
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.endswith(".tif") or filename.endswith(".tiff"):
            # 构建完整的文件路径
            tif_path = os.path.join(input_folder, filename)
            # 构建输出文件的路径
            png_filename = os.path.splitext(filename)[0] + ".png"
            png_path = os.path.join(output_folder, png_filename)

            # 打开 TIFF 文件并保存为 PNG 文件
            with Image.open(tif_path) as img:
                img.save(png_path, "PNG")
            print(f"Converted {tif_path} to {png_path}")


# 指定输入和输出文件夹
input_folder = "/Users/qingrui/Desktop/TOOTH_DAMAGE_DATASET/no_damage"
output_folder = "/Users/qingrui/Desktop/TOOTH_DAMAGE_DATASET/no_damage_png"

convert_tif_to_png(input_folder, output_folder)
