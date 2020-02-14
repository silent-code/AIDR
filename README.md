
# AI-powered Assault Interdiction Detection and Recognition (AIDR)


| AIDR Assault Detected on Jetson Nano (4 FPS)                                   | Normal Activity Detected                          |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![image](https://github.com/silent-code/AIDR/blob/master/output/gifs/assault1.gif) | ![image](https://github.com/silent-code/AIDR/blob/master/output/gifs/walking.gif)|



This repository currently implemented the CPM and Hourglass model using TensorFlow. Instead of normal convolution, inverted residuals (also known as Mobilenet V2) module has been used inside the model for **real-time** inference. 


The respository contains:

* Code of training cpm & hourglass model
* Android demo source code (thanks to [littleGnAl](https://github.com/littleGnAl))
* iOS demo source code (thanks to [tucan](https://github.com/tucan9389))

## Hardware 
![alt text][image_1]: ./images/IMG_6120.JPG


## Training

***

### Dependencies:

* Python3
* TensorFlow >= 1.4
* Opencv

### Dataset:

Training dataset available through [google driver](https://drive.google.com/open?id=1zahjQWhuKIYWRRI2ZlHzn65Ug_jIiC4l).

Unzip it will obtain the following file structure

```bash
# root @ ubuntu in ~/hdd/ai_challenger
$ tree -L 1 .
.
├── ai_challenger_train.json
├── ai_challenger_valid.json
├── train
└── valid
```

The traing dataset only contains single person images and it come from the competition of [AI Challenger](https://challenger.ai/datasets/keypoint). 

* 22446 training examples
* 1500 testing examples

I transfer the annotation into COCO format for using the data augument code from [tf-pose-estimation](https://github.com/ildoonet/tf-pose-estimation) respository.

### Hyper-parameter

In training procedure, we use `cfg` file on `experiments` folder for passing the hyper-parameter.

Below is the content of [mv2_cpm.cfg](https://github.com/edvardHua/PoseEstimationForMobile/blob/master/training/experiments/mv2_cpm.cfg).

```bash
[Train]
model: 'mv2_cpm'
checkpoint: False
datapath: '/root/hdd/ai_challenger'
imgpath: '/root/hdd/'
visible_devices: '0, 1, 2'
multiprocessing_num: 8
max_epoch: 1000
lr: '0.001'
batchsize: 5
decay_rate: 0.95
input_width: 192
input_height: 192
n_kpoints: 14
scale: 2
modelpath: '/root/hdd/trained/mv2_cpm/models'
logpath: '/root/hdd/trained/mv2_cpm/log'
num_train_samples: 20000
per_update_tensorboard_step: 500
per_saved_model_step: 2000
pred_image_on_tensorboard: True
```

The cfg not cover all the parameters of the model, there still have some parameters in the `network_mv2_cpm.py`.

### Train by nvidia-docker

Build the docker by the following command:

```bash
cd training/docker
docker build -t single-pose .
```
or

```
docker pull edvardhua/single-pose
```

Then run the following command to train the model:

```bash
nvidia-docker run -it -d \
-v <dataset_path>:/data5 -v <training_code_path>/training:/workspace \
-p 6006:6006 -e LOG_PATH=/root/hdd/trained/mv2_cpm/log \
-e PARAMETERS_FILE=experiments/mv2_cpm.cfg edvardhua/single-pose
```

Also, it will create the tensorboard on port 6006. Beside, make sure you install the `nvidia-docker`.

### Train by ordinary way

0. (mac only) Change tensorflow-gpu==1.4.0 to tensorflow==1.4.0 on requirements.txt.

1. install the dependencies.

```bash
cd training
pip3 install -r requirements.txt
```

Beside, you also need to install [cocoapi](https://github.com/cocodataset/cocoapi)

2. Edit the parameters files in experiments folder, it contains almost all the hyper-parameters and other configuration you need to define in training. After that, passing the parameters file to start the training:

```bash
cd training
python3 src/train.py experiments/mv2_cpm.cfg
```

After 12 hour training, the model is almost coverage on 3 Nvidia 1080Ti graphics cards, below is the corresponding plot on tensorboard.

![image](https://github.com/edvardHua/PoseEstimationForMobile/raw/master/images/loss_lastlayer_heat.png)

### Bechmark (PCKh)

Run the follow command to evaluate the value of your PCKh.

```bash
python3 src/benchmark.py --frozen_pb_path=hourglass/model-360000.pb \
--anno_json_path=/root/hdd/ai_challenger/ai_challenger_valid.json \
--img_path=/root/hdd \
--output_node_name=hourglass_out_3
```




## Reference

***
Original Pyimagesearch tutorial on Keras video classification: https://www.pyimagesearch.com/2019/07/15/video-classification-with-keras-and-deep-learning/

Configuring Jetson Nano: https://www.pyimagesearch.com/2019/05/06/getting-started-with-the-nvidia-jetson-nano/

Increasing swap memory and installing Jetcam: https://thenewstack.io/tutorial-configure-nvidia-jetson-nano-as-an-ai-testbed/

Install Opencv on Nano: https://pythops.com/post/compile-deeplearning-libraries-for-jetson-nano

## License

***

[Apache License 2.0](https://github.com/edvardHua/PoseEstimationForMobile/blob/master/LICENSE)
