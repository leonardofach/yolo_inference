# Script to install Yolov5 (Ultralytics)
# by Leonardo Fachetti Jovêncio

import os

# Cloning the Yolov5 repository from Github
os.system("git clone https://github.com/ultralytics/yolov5")

# Installing the necessary dependencies
os.system("pip install -r requirements.txt")  # Ignore error messages


# Replacing Ultralytics' detect.py file with my modified detect.py file
'''
I added a few lines of code in the detect.py file so that, in addition to
detection, it also saves the detection times per image in a txt file.

This file is called times_inf.txt and is saved in the runs/detect/exp_ directory
'''
os.system("rm yolov5/detect.py")
os.system("cp detect.py yolov5/detect.py")
