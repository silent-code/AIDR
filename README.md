[image_1]: ./images/IMG_6120.JPG
# AI-powered Assault Interdiction Detection and Recognition (AIDR)


| AIDR Assault Detected on Jetson Nano (4 FPS)                                   | Normal Activity Detected                          |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![image](https://github.com/silent-code/AIDR/blob/master/output/gifs/assault1.gif) | ![image](https://github.com/silent-code/AIDR/blob/master/output/gifs/walking.gif)|



AIDR is an edge computing device utilizing the Jetson Nano and Keras/Tensorflow-based automated human activity recognition to provide smart cities with ad-hoc video based neighborhood watch services to support assault/robbery in progress assessment, public safety, property protection, etc. The system can be implmented for example on forwar- and reverse-view car cameras, in exhisitng cctv networks or stand-alone mounted systems. Such a smart city adhoc video anaytic criminal activity monitor system addresses public privacy concerns by automating the detection and recognition of person/property assault by live monitoring video feeds, not recording video and eliminating human-in-the-loop involvement when normal activity is detected.


The respository contains:

* Code for training and inferencing on the Jetson Nano
* 
* iOS demo source code (thanks to [tucan](https://github.com/tucan9389))

## Hardware 
Jetson Nano and either csi or usb camera


![](https://github.com/silent-code/AIDR/blob/master/images/IMG_6120.JPG =250x250)


## Training

***

### Dependencies:

* Python3
* TensorFlow >= 1.4
* Opencv

### Dataset:

Download link in References section below.

Data Distribution
Training set: 11524

Validation set: 2881

Model
Resnet-50

Data Augmentations
The following data augmentation has been applied to increase the no of images in the training set

Flip horizontal
Lighting
Zooming
Warping


## Reference

***
Original Pyimagesearch tutorial on Keras video classification: https://www.pyimagesearch.com/2019/07/15/video-classification-with-keras-and-deep-learning/

Configuring Jetson Nano: https://www.pyimagesearch.com/2019/05/06/getting-started-with-the-nvidia-jetson-nano/

Increasing swap memory and installing Jetcam: https://thenewstack.io/tutorial-configure-nvidia-jetson-nano-as-an-ai-testbed/

Install Opencv on Nano: https://pythops.com/post/compile-deeplearning-libraries-for-jetson-nano

Dataset: https://www.dropbox.com/s/0jp57lhs0y805ro/sports-type-classifier-data.7z?dl=0

## License

***

[Apache License 2.0](https://github.com/edvardHua/PoseEstimationForMobile/blob/master/LICENSE)
