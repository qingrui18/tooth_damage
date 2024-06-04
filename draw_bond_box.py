import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import pyplot as plt




def draw_bond_box(img_path,annotation_path):

  file = open(annotation_path, 'r')
  lines = file.readlines() #read the first line of the annotation

  for line in lines:
    first_line = line.split() #split the first line by the empty space

    x_center, y_center,width,height = (float(first_line[1]),float(first_line[2]),
                                       float(first_line[3]),float(first_line[4]))


    # Add the bonding box of the annotated area
    img = cv2.imread(img_path)  # img is a np.array with shape (h, w, c)
    width_actual,height_actual = img.shape[1],img.shape[0]

    box_left_top = np.array([width_actual*(x_center-width/2), height_actual*(y_center-height/2)])      # bbox左上角坐标
    box_right_bottom =np.array([width_actual*(x_center+width/2), height_actual*(y_center+height/2)])   # bbox右下角坐标

    line_color = (0, 255, 0)
    line_thickness = 2
    line_type = 4

    cv2.rectangle(img, tuple(box_left_top.astype(int)), tuple(box_right_bottom.astype(int)), line_color, line_thickness, line_type)  # 画bbox


    # Add text background
    if first_line[0] == '2':
      class_name = 'damage require repair'

    if first_line[0] == '3':
      class_name = 'damage NOT require repair'

    if first_line[0] == '0':
      class_name = 'distal area'

    fontFace = cv2.FONT_HERSHEY_PLAIN
    fontScale = 1
    thickness = 1
    text_size = cv2.getTextSize(class_name,fontFace,fontScale,thickness)[0]  #Get the text size
    text_right_bottom = box_left_top + np.array(list(text_size)) #Get the coordinates of the right bottom of the text
    cv2.rectangle(img, tuple(box_left_top.astype(int)), tuple(text_right_bottom.astype(int)),  line_color, -1)  # drawing the text background


    # Add the text
    box_left_top[1] = box_left_top[1] + (text_size[1]/2 + 4)   # 计算文字起始位置偏移
    text_color = tuple(int(x) for x in 255 - np.array(line_color))
    cv2.putText(img, class_name , tuple(box_left_top.astype(int)), cv2.FONT_HERSHEY_PLAIN, 1.0, text_color, 1)  # 绘字

    cv2_imshow(img)

  return