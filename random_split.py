import random
import os
import shutil


def random_split(list_path, ratio, shuffle=True):
    full_list = os.listdir(list_path)
    n_total = len(full_list)
    offset = int(n_total * ratio)

    if n_total == 0 or offset < 1:
        return [], full_list

    if shuffle:
        random.shuffle(full_list)

    sublist_1 = full_list[:offset]
    sublist_2 = full_list[offset:]

    return sublist_1, sublist_2


if __name__ == "__main__":
    data = '/Users/qingrui/Desktop/source_data/images_DR_only'
    sub_data1, sub_data2 = random_split(data, ratio=0.8, shuffle=True)
    print('The length of the training set is: ', len(sub_data1))
    print('The length of the validation set is: ', len(sub_data2))

    # training set
    for sub_data in sub_data1:
        # images
        src = os.path.join(data, sub_data)
        dst = '/Users/qingrui/Desktop/YOLOV8_TOOTH_DAMAGE/full_area_DR_only/images/train'
        #print(src, dst)
        shutil.copy(src, dst)

        # annotations
        src_label = '/Users/qingrui/Desktop/source_data/annotations_DR_only/' + sub_data.strip('.tif') + '.txt'
        dst_label = '/Users/qingrui/Desktop/YOLOV8_TOOTH_DAMAGE/full_area_DR_only/labels/train'
        #print(src_label, dst_label)
        shutil.copy(src_label, dst_label)

    # validation set
    for sub_data in sub_data2:
        # images
        src = os.path.join(data, sub_data)
        dst = '/Users/qingrui/Desktop/YOLOV8_TOOTH_DAMAGE/full_area_DR_only/images/val'
        #print(src, dst)
        shutil.copy(src, dst)

        # annotations
        src_label = '/Users/qingrui/Desktop/source_data/annotations_DR_only/' + sub_data.strip('.tif') + '.txt'
        dst_label = '/Users/qingrui/Desktop/YOLOV8_TOOTH_DAMAGE/full_area_DR_only/labels/val'
        #print(src_label, dst_label)
        shutil.copy(src_label, dst_label)


