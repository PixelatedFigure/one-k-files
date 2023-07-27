import os
import shutil

dir = "files/"

for file in os.listdir(dir):
    lang = file.split('-', 1)[0]

    to = dir + lang
    
    if not os.path.exists(to):
        os.makedirs(to)

    if os.path.exists(to):
        file_path = dir + file
        shutil.move(file_path, to)