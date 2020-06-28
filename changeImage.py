#!/usr/bin/env python3

from PIL import Image
import os
import getpass

size = 600, 400

path = '/home/' + getpass.getuser() + '/supplier-data/images/'
files = os.listdir(path)

for item in files:
    try:
        image_file = Image.open(path + item, 'r').convert("RGB")
        new_image = image_file.resize(size)
        file_name = item.split('.')
        new_image.save(path + file_name[0] + '.jpeg', "JPEG")
    except:
        None
