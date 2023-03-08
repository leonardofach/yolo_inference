# Script for Yolov5 (Ultralytics) detection time inference
# by Leonardo Fachetti Jovêncio

'''
The detect.py program generates a txt file called "times_inf.txt" inside the directory where the results
of the detection were saved (runs/detect/exp..). This file contains the times (in seconds) of detection of
each image from the given dataset. This script reads these times and generates the graphs
boxplot and confidence interval.
'''

import argparse
import numpy as np
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser(description='''This script reads the times_inf.txt file (located in 
runs/detect/exp_ which contains the detection times of each image from the dataset informed in the 
detect.py program call) and generates the graphs boxplot and confidence interval.''')

parser.add_argument("--file", action="store", dest="file",
                    default="", required=True, help="File containing the detection times per image.")

parser.add_argument("--name", action="store", dest="name",
                    default="", required=True, help='''Name of the analyzed dataset to be included in
the description of the images referring to the generated graphics.''')

arguments = parser.parse_args()

# Reading the contents of times_inf.txt file
file_times_inf = open(str(arguments.file), "r")
lines = file_times_inf.readlines()
file_times_inf.close()

times = []
total_samples = 0
for c in lines:
    times.append(1000 * (float(c[:-2])))  # Changing to milliseconds
    total_samples += 1

mean = np.mean(times)
median = np.median(times)
std = np.std(times)

# Generating the boxplot graph
plt.figure(figsize=(10, 8))
plt.style.use("bmh")
plt.boxplot(times)
plt.title("Detection time yolov5")
plt.ylabel("Time (ms)")
plt.xlabel("Samples")
plt.savefig(str(arguments.name) + "_box_plot.png", format="png")


# Generating the confidence interval graph
'''
80% -> 1.28
90% -> 1.645
95% -> 1.96
98% -> 2.33
99% -> 2.58
'''
error = 1.96 * (std / np.sqrt(total_samples))
plt.figure(figsize=(10, 8))
plt.style.use("bmh")
plt.errorbar("Samples", mean, yerr=error, color="blue", fmt='o', label=f"Mean: {mean}")
plt.scatter("Samples", (mean + error), color="blue", label=f"Max: {mean + error}")
plt.scatter("Samples", (mean - error), color="blue", label=f"Min: {mean - error}")
plt.legend()
plt.title("Detection time yolov5")
plt.ylabel("Time (ms)")
plt.savefig(str(arguments.name) + "_conf_interval.png", format="png")
