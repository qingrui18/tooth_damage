import os


def rename_files_to_match_tiff(tiff_folder, other_folder):
    # 获取tiff文件夹中所有的tiff文件名
    tiff_files = [f for f in os.listdir(tiff_folder) if f.endswith(".tif")]

    # 获取其他文件夹中所有的非tiff文件名
    other_files = [f for f in os.listdir(other_folder) if not f.endswith(".tif")]

    for tiff_file in tiff_files:
        # 获取 tiff 文件的前缀部分
        tiff_prefix = os.path.splitext(tiff_file)[0]

        for other_file in other_files:
            # 获取文件的扩展名
            ext = os.path.splitext(other_file)[1]
            # 找到包含匹配前缀的文件
            if tiff_prefix in other_file:
                # 构建新的文件名
                new_filename = tiff_prefix + ext
                # 获取完整的文件路径
                old_file = os.path.join(other_folder, other_file)
                new_file = os.path.join(other_folder, new_filename)
                # 重命名文件
                os.rename(old_file, new_file)
                print(f"Renamed {other_file} to {new_filename}")


# 指定TIFF文件夹和其他文件夹路径
tiff_folder = "/Users/qingrui/Desktop/TOOTH_DAMAGE_DATASET/no_damage"
other_folder = "/Users/qingrui/Desktop/train/images"

rename_files_to_match_tiff(tiff_folder, other_folder)
