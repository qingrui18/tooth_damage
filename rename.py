import os

def rename_files(folder_path):
    for filename in os.listdir(folder_path):
        if '_png' in filename:
            # 找到 `_png` 的位置并删除其后的字符
            base_name = filename.split('_png')[0]
            new_filename = base_name + '.txt'
            # 获取完整的文件路径
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, new_filename)
            # 重命名文件
            os.rename(old_file, new_file)
            print(f"Renamed {filename} to {new_filename}")

# 指定文件夹路径
folder_path = "/Users/qingrui/Desktop/test/new_ann"

rename_files(folder_path)
