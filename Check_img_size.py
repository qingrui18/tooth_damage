import os
from PIL import Image
import numpy as np


def get_image_files(root_dir, extensions=['.tif', '.png']):
    image_files = []
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                image_files.append(os.path.join(subdir, file))
    return image_files


def calculate_average_resolution(image_files):
    total_width = 0
    total_height = 0
    num_images = len(image_files)

    for image_file in image_files:
        with Image.open(image_file) as img:
            width, height = img.size
            total_width += width
            total_height += height

    if num_images == 0:
        return (0, 0)

    average_width = total_width / num_images
    average_height = total_height / num_images

    return (average_width, average_height)


if __name__ == "__main__":
    root_dir = input("Enter the root directory path: ")
    image_files = get_image_files(root_dir)

    if not image_files:
        print("No .tif or .png files found.")
    else:
        avg_width, avg_height = calculate_average_resolution(image_files)
        print(f"Average Width: {avg_width:.2f}")
        print(f"Average Height: {avg_height:.2f}")
        print(f"Number of Images: {len(image_files)}")
