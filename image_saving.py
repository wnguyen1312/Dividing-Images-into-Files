#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Updated on Thurs 19.02.2023

@author: williamnguyen & urvinath
"""

import os
from os.path import exists, join, splitext
from shutil import move
import logging

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Supported image types
image_extensions = [".jpg", ".jpeg", ".png", ".tif", ".tiff"]

# Input from user
angle_inc = float(input('Please enter your angle increment (e.g., 5): '))
dir_path = input('Please enter the directory of your record loop images: ')
number_frames = int(input('Please enter the number of frames per rotation (e.g., 19): '))

if not os.path.isdir(dir_path):
    logging.error(f"The directory '{dir_path}' does not exist.")
    exit(1)

# Function to make filenames unique
def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    while exists(f"{dest}/{name}"):
        name = f"{filename}({counter}){extension}"
        counter += 1
    return name

# Function to move files
def move_file(dest, entry, name):
    if exists(join(dest, name)):
        unique_name = make_unique(dest, name)
        move(entry, join(dest, unique_name))
    else:
        move(entry, join(dest, name))

# Count total valid image files in the directory
def count_images(directory):
    return sum(1 for path in os.listdir(directory) if splitext(path)[1].lower() in image_extensions)

total_images = count_images(dir_path)
logging.info(f"Total number of valid image frames: {total_images}")

# Processing images into folders
count = 0
j = 1

while number_frames * j <= total_images:
    folder_name = f"{j * angle_inc:.1f}"  # Folder name based on angle increment
    new_dir = join(dir_path, folder_name)

    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    for _ in range(number_frames):
        count += 1
        padded_count = f"{count:04d}"
        image_name = join(dir_path, f"{padded_count}.tif")

        if os.path.exists(image_name):
            move_file(new_dir, image_name, os.path.basename(image_name))
        else:
            logging.warning(f"File {image_name} not found.")

    logging.info(f"Processed images for folder: {folder_name}")
    j += 1

logging.info("Done! The images have been saved in different folders.")
