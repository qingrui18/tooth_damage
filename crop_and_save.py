import os
from PIL import Image


def auto_crop(img_path, annotation_path):
    file = open(annotation_path, 'r')
    lines = file.readlines()
    distal_annotation = []

    for line in lines:
        # crop the area based on the number: '0' is distal area, '2': damage require restoration, '3': damage not
        # require restoration
        if line[0] == '0':
            distal_annotation = line
            break

    # split the first line by the empty space
    distal_annotation = distal_annotation.split()

    # get the parameters of the bonding box
    x_center, y_center, width, height = (float(distal_annotation[1]),
                                         float(distal_annotation[2]),
                                         float(distal_annotation[3]),
                                         float(distal_annotation[4]))
    file.close()

    img = Image.open(img_path)
    width_actual, height_actual = img.size

    # cropped area = [left,top,right,bottom]
    left, top, right, bottom = (int(width_actual * (x_center - width / 2)),
                                int(height_actual * (y_center - height / 2)),
                                int(width_actual * (x_center + width / 2)),
                                int(height_actual * (y_center + height / 2)))

    cropped_area = (left, top, right, bottom)
    cropped_img = img.crop(cropped_area)

    # Shows the image in image viewer
    # display(cropped_img)

    return cropped_img


def crop_and_save(input_path, output_path):
    image_folder = input_path + '/images'
    annotation_folder = input_path + '/annotations'
    images = os.listdir(image_folder)

    for image in images:

        if image == '.DS_Store':
            continue

        # print(image)
        cropped_image = auto_crop(image_folder + '/' + image, annotation_folder + '/' + image.strip('.tif') + '.txt')
        cropped_image.save(output_path + '/' + image)


if __name__ == '__main__':
     crop_and_save('/Users/qingrui/Desktop/TOOTH_DAMAGE_DATASET/no_damage',
                   '/Users/qingrui/Desktop/bk_crop')
