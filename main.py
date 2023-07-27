import os
import shutil

dir = "files/"

for file in os.listdir(dir):
    dir_name = file.split('-', 1)[0]

    dir_path = dir + dir_name
    
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    if os.path.exists(dir_path):
        file_path = dir + file
        shutil.move(file_path, dir_path)