# Directory Enumeration

import requests
import sys

dir_list = open("dirlist.txt").read()
directories = dir_list.splitlines()

for dir in directories:
    dir_enum = f"http://{sys.argv[1]}/{dir}.*"
    r = requests.get(dir_enum)
    if r.status_code == 404:
        pass
    else:
        print("Valid Directory: ", dir_enum)
