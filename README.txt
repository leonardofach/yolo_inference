Script to evaluate yolo detection time
by Leonardo Fachetti Jovencio


The yolo_install.py file installs yolov5 provided by Ultralytics (https://github.com/ultralytics/yolov5),
installs the necessary dependencies and replaces the detect.py file from the Ultralytics repository with the
detect.py from this repository, in the which added a few lines of code to save the detection times of each image in a txt file.


The plot_graphs.py file reads this txt file containing the detection times of each image and generates the boxplot
and confidence interval graphs.