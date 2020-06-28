#!/usr/bin/env python3

import requests
import os
import getpass

url = "http://localhost/upload/"
path = "/home/" + getpass.getuser() + "/supplier-data/images/"
files = os.listdir(path)

for file_name in files:
    try:
        file_to_upload = file_name.split('.')
        if file_to_upload[1] == 'jpeg':    
            print(file_name)
            with open(path + file_name, 'rb') as opened:
                r = requests.post(url, files={'file': opened})
    except IndexError:
        None

