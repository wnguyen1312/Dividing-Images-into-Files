#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 12:10:09 2022

@author: williamnguyen & urvinath
"""

#-------------------------------------------------------------------#

#Please put in what you want here

angleInc = float(input('Please enter your angle increment e.g 5: ')) #your angle increment e.g 5 degrees 
dir_path = str(input('Please enter the directory of your record loop images: '))
number_frames = int(input('Please enter the number of frames per rotation e.g 19, 18, 17: '))

#-------------------------------------------------------------------#


import os 
from os import rename
from os.path import splitext, exists, join
from shutil import move
import os.path


image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]


  

def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # * IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name


def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry, dest)
    
#function to count the number of images in the folder

count = 0
total =0

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        total += 1
print('Total number of frames:', total)


#renaming the first 9 frames if total < 1000 

if total < 1000: 
    for i in range(1,10):
        old_name = dir_path + '//' + '00' + str(i) + '.tif'
        new_name = dir_path + '//' + '0' + str(i) + '.tif'
        rename(old_name, new_name)
else:
    pass


j=1

while number_frames*j <= total:
    for path in os.listdir(dir_path):
        
         if os.path.isfile(os.path.join(dir_path, path)):
             count +=1
             
             if count==number_frames*j:
                 newpath = ''+str(j*angleInc)
                 newpath = dir_path+str(j*angleInc)
                 os.makedirs(newpath)
                 j=j+1
                 
                 for i in range(number_frames):
                     new_count = count-i
                     if os.path.exists(dir_path+'//'+str(new_count)+'.tif')==True:
                         oldpath = dir_path+'//'+str(new_count)+'.tif'

                         move_file(newpath,oldpath,oldpath) 
                     else: 
                         oldpath = dir_path+'//'+"0"+str(new_count)+'.tif'

                         move_file(newpath,oldpath,oldpath)

print('Done!. The images SHOULD be saved in different folders now.')