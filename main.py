# Script to create the different Yolov8 networks and perform the inference
# By Leonardo Fachetti Jovêncio

#pip install ultralytics
from ultralytics import YOLO
import argparse
import os

parser = argparse.ArgumentParser(description='''This script creates the
Yolo network and performs detection on the provided dataset.''')

parser.add_argument("--dataset", action="store", dest="dataset",
                    default="", required=True, help="Dataset to be detected.")

parser.add_argument("--model", action="store", dest="model",
                    default="", required=True, help="Yolo network template to use.")

arguments = parser.parse_args()


# Loading a pretrained YOLO model
model = YOLO (arguments.model)

# Detection
results = model.predict(arguments.dataset, save_txt=True, save_conf=True, conf=0.5)

# models
'''
yolov8n.pt
yolov8s.pt
yolov8m.pt
yolov8l.pt
yolov8x.pt
'''

# Saving inference times for each image in a txt file
times = []
for c in range (0, len (results)):
  times.append (str(results[c].speed ["inference"]))

file_times = open ("times.txt", "a")
for c in times:
  file_times.write (c + "\n")
file_times.close ()

# Creating a directory with the name of the informed hardware to save all results
os.system (f"mkdir {arguments.model[:-3]}")
os.system (f"mv *.txt {arguments.model[:-3]}")
os.system (f"mv runs/detect/predict/labels {arguments.model[:-3]}")
os.system ("rm -r runs")
os.system (f"rm {arguments.model}")