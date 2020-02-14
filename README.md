[image_1]: ./images/IMG_6120.JPG
[image_2]: ./images/IMG_6119.JPG

# AI-powered Assault Interdiction Detection and Recognition (AIDR)


| AIDR Assault Detected on Jetson Nano (4 FPS)                                   | Normal Activity Detected                          |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![image](https://github.com/silent-code/AIDR/blob/master/output/gifs/assault1.gif) | ![image](https://github.com/silent-code/AIDR/blob/master/output/gifs/walking.gif)|



AIDR is an edge-compute platform utilizing the Jetson Nano and Keras/Tensorflow-based automated human activity recognition to provide smart cities with ad-hoc, video based neighborhood watch services to support assault/robber-in-progress assessment, public safety, property protection, etc. The system can be implemented for example on forward- and reverse-view car cameras, with existing cctv networks or stand-alone mounted systems. Such a smart city adhoc video anaytic criminal activity monitor system addresses public privacy concerns by automating the detection and recognition of person/property assault by live monitoring video feeds, not recording video and eliminating human-in-the-loop involvement when normal activity is detected.


The respository contains:

* Code for training (train.py) and inferencing (predict_camera.py) on the Jetson Nano
* Example video clips to use for inferencing source
* A serialized model trained on the sports activity dataset
* A label pickle
* An install script for systemd startup service for the AIDR application

## Hardware 
Jetson Nano and either csi or usb camera:


![alt text][image_1]

Example image of the AIDR mounted in forward view camera position on vehicle dash:

![alt text][image_2]


## Critical Dependencies:

* Python3
* Tensorflow GPU >= 1.13.1
* Keras > 2.3.1e
* Opencv > 4.1.0

## Training 

***Dataset:

Data Download link in References section below.

Data Distribution
Training set: 11524

Validation set: 2881

**Model:
Resnet-50

**Data Augmentations
The following data augmentation has been applied to increase the no of images in the training set

Flip horizontal
Lighting
Zooming
Warping


## Reference

***
Dataset: https://www.dropbox.com/s/0jp57lhs0y805ro/sports-type-classifier-data.7z?dl=0

Original Pyimagesearch tutorial on Keras video classification: https://www.pyimagesearch.com/2019/07/15/video-classification-with-keras-and-deep-learning/

Configuring Jetson Nano: https://www.pyimagesearch.com/2019/05/06/getting-started-with-the-nvidia-jetson-nano/

Increasing swap memory and installing Jetcam: https://thenewstack.io/tutorial-configure-nvidia-jetson-nano-as-an-ai-testbed/

Install Opencv on Nano: https://pythops.com/post/compile-deeplearning-libraries-for-jetson-nano

Nano case: https://www.amazon.com/gp/product/B07ZNVH982/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1

CSI cam: https://www.amazon.com/gp/product/B07VFFRX4C/ref=ppx_yo_dt_b_asin_title_o03_s01?ie=UTF8&psc=1

USB cam: https://bluerobotics.com/store/sensors-sonars-cameras/cameras/cam-usb-low-light-r1/

## License

***

[Apache License 2.0](https://github.com/edvardHua/PoseEstimationForMobile/blob/master/LICENSE)
