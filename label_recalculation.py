import os


def annotations_recalculation(input_path, output_path):
    labels = ['2', '3']
    distal = ['0']
    annotations = os.listdir(input_path)

    for annotation in annotations:
        print(annotation)

        if annotation == '.DS_Store':
            continue

        file = open(input_path + '/' + annotation, 'r')
        lines = file.readlines()

        new_lines = []

        for line in lines:
            if line[0] in labels:
                new_lines.append(line)

            if line[0] in distal:
                line_distal = line.split()
                x_distal, y_distal, width_distal, height_distal = (float(line_distal[1]), float(line_distal[2]),
                                                                   float(line_distal[3]), float(line_distal[4]))
        file.close()

        recalculated_lines = []

        for line in new_lines:
            line_damage = line.split()

            x_damage, y_damage, width_damage, height_damage = (float(line_damage[1]), float(line_damage[2]),
                                                               float(line_damage[3]), float(line_damage[4]))

            x_damage = (x_damage - (x_distal - width_distal / 2)) / width_distal
            y_damage = (y_damage - (y_distal - height_distal / 2)) / height_distal

            width_damage = width_damage / width_distal
            height_damage = height_damage / height_distal

            line_damage[1] = str(x_damage)
            line_damage[2] = str(y_damage)
            line_damage[3] = str(width_damage)
            line_damage[4] = str(height_damage)

            line_damage = ' '.join(line_damage)
            recalculated_lines.append(line_damage + '\n')

        print(recalculated_lines)

        file = open(output_path + '/' + annotation, 'w')
        file.writelines(recalculated_lines)
        file.close()

if __name__ == '__main__':
    annotations_recalculation(input_path='/Users/qingrui/Desktop/TOOTH_DAMAGE_DATASET/damage_not_require_restoration/annotations',
                               output_path='/Users/qingrui/Desktop/distal_scale_annotations/damage_not_require_restoration')
