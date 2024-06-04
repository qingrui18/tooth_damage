import os
import sys


def change_the_label(input_path, output_path):
    annotations = os.listdir(input_path)

    for annotation in annotations:
        print(annotation)

        if annotation == '.DS_Store':
            continue

        file = open(input_path + '/' + annotation, 'r')
        lines = file.readlines()
        new_lines = []

        for line in lines:
            if line[0] == '0':
                print(line)
                line = line.replace("0","2",1)
                print(line)

            #if line[0] == '3':
                #print(line)
                #line = line.replace("3","1",1)
                #print(line)

            new_lines.append(line)

        file.close()

        file = open(output_path + '/' + annotation, 'w')
        file.writelines(new_lines)
        file.close()

if __name__ == '__main__':
    change_the_label('/Users/qingrui/Desktop/no_damage/train/labels',
                     '//Users/qingrui/Desktop/no_damage/labels')