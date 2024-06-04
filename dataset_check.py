import os
import sys


# The aim of this function is to check the one-to-one correspondence of the damage folder
def check_correspondence(img_folder, annotation_folder):
    images = os.listdir(img_folder)
    annotations = os.listdir(annotation_folder)

    images.sort()
    annotations.sort()

    if '.DS_Store' in images:
        images.remove('.DS_Store')

    if '.DS_Store' in annotations:
        annotations.remove('.DS_Store')

    print(len(images))
    print(len(annotations))

    num = 0
    for annotation in annotations:

        if annotation == '.DS_Store':
            continue

        annotation_id = annotation.strip('.txt') + '.tif'

        if annotation_id not in images:
            num += 1
            print(annotation, "does not have a image")
    print("\n", num, " file(S) is(are) not have correspond image", sep="")


# The aim of this function is to check if there are files that appear in both damage_not_require_restoration folder and
# damage_require_restoration folder
def check_intersection(path_1, path_2):
    damage_not_require_restoration = os.listdir(path_1)
    damage_require_restoration = os.listdir(path_2)

    damage_not_require_restoration.sort()
    damage_require_restoration.sort()

    if '.DS_Store' in damage_not_require_restoration:
        damage_not_require_restoration.remove('.DS_Store')

    if '.DS_Store' in damage_require_restoration:
        damage_require_restoration.remove('.DS_Store')

    set1 = set(damage_not_require_restoration)
    set2 = set(damage_require_restoration)

    if set1 & set2:
        print("Two lists have intersection")
        print(list(set1.intersection(set2)))
    else:
        print("Two lists do not have intersection")


if __name__ == "__main__":
    check_correspondence('/Users/qingrui/Desktop/TOOTH_DAMAGE_DATASET/no_damage/images_as_class_tif',
                         '/Users/qingrui/Desktop/TOOTH_DAMAGE_DATASET/no_damage/labels_as_class')


    #check_intersection(
     #   '/Users/qingrui/Desktop/no_damage/images',
     #   '/Users/qingrui/Desktop/no_damage/annotations')

    # check num of files
    #images = os.listdir('/Users/qingrui/Desktop/tooth_damage_classification_machine_learning/DR_cropped_images')
    #print(len(images))



