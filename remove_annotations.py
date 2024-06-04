import os


def remove_annotations(input_path, output_path):
    labels = ['2', '3']
    annotation_folder = input_path
    annotations = os.listdir(annotation_folder)

    for annotation in annotations:

        file = open(input_path + '/' + annotation, 'r')
        lines = file.readlines()
        new_lines = []

        for line in lines:
            if line[0] in labels:
                new_lines.append(line)

        file.close()

        file = open(output_path + '/' + annotation, 'w')
        file.writelines(new_lines)
        file.close()


# if __name__ == '__main__':
#     remove_annotations('','')