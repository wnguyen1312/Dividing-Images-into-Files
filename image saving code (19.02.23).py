#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Updated on Thurs 19.02.2023

@author: williamnguyen & urvinath
"""

#-------------------------------------------------------------------#

#Please put in what you want here

angleInc = float(input('Please enter your angle increment e.g 5: ')) #your angle increment e.g 5 degrees 
dir_path = str(input('Please enter the directory of your record loop images. E.g E:\\Xingjian Hou\\SavingImgTest\\test: '))
number_frames = int(input('Please enter the number of frames per rotation e.g 19, 18, 17: '))

#-------------------------------------------------------------------#


import time
import os 
from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
from itomUi import ItomUi
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os.path


# ? supported image types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# ? supported Video types
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
# ? supported Audio types
audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]
# ? supported Document types
document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]


#---------------------------

  

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
                     
                     if new_count < 10 :
                         image_name = dir_path+'//'+'000'+str(new_count)+'.tif'
                     elif new_count < 100: 
                         image_name = dir_path+'//'+'00'+str(new_count)+'.tif'
                     elif new_count < 1000:  
                        image_name = dir_path+'//'+'0'+str(new_count)+'.tif'
                     else: 
                        image_name = dir_path+'//'++str(new_count)+'.tif'
                        
                     if os.path.exists(image_name)==True:
                         oldpath = dir_path+'//'+str(new_count)+'.tif'

                         move_file(newpath,oldpath,oldpath) 
                     else: 
                         
                         oldpath = dir_path+'//'+"0"+str(new_count)+'.tif'

                         move_file(newpath,oldpath,oldpath)

print('Done!. The images SHOULD be saved in different folders now.')