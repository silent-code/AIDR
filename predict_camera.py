# USAGE
# python predict_camera.py --model model/activity.model --input example_clips/assault.mp4 --label-bin model/lb.pickle --output output/assault1.avi --size 100


# import the necessary packages
from keras.models import load_model
from collections import deque
import numpy as np
import argparse
import pickle
import cv2
import time
from jetcam.csi_camera import CSICamera
from jetcam.usb_camera import USBCamera

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
	help="path to trained serialized model")
ap.add_argument("-l", "--label-bin", required=True,
	help="path to  label binarizer")
ap.add_argument("-i", "--input", required=True,
	help="path to our input video")
ap.add_argument("-o", "--output", required=True,
	help="path to our output video")
ap.add_argument("-s", "--size", type=int, default=128,
	help="size of queue for averaging")
args = vars(ap.parse_args())

record_output = 0
use_video_as_input = 0
training = 0
save_frames_to_dir = '/home/tim/python_scripts/machine-learning-pipeline-Keras-video-classification/Sports-Type-Classifier/data/standing/'

# load the trained model and label binarizer from disk
print("[INFO] loading model and label binarizer...")
model = load_model(args["model"])
lb = pickle.loads(open(args["label_bin"], "rb").read())

# initialize the image mean for mean subtraction along with the
# predictions queuesave_frames_to_dir
mean = np.array([123.68, 116.779, 103.939][::1], dtype="float32")
Q = deque(maxlen=args["size"])

# initialize the video stream, pointer to output video file, and
# frame dimensions

if use_video_as_input:
	vs = cv2.VideoCapture(args["input"])
else:
	#vs = CSICamera(width=224, height=224, capture_width=1080, capture_height=720, capture_fps=30)
	vs = USBCamera(capture_device=0)

writer = None
(W, H) = (None, None)

# Start time
start = time.time()

# loop over frames from the video file stream
count = 0
# whileTrue:
for count in range(0,700):
	# read the next frame from the file
	if use_video_as_input:
		(grabbed, frame) = vs.read()
	else:
		frame = vs.read()

	# if the frame was not grabbed, then we have reached the end
	# of the stream
	#if not grabbed:
	#	break

	# if the frame dimensions are empty, grab them
	if W is None or H is None:
		(H, W) = frame.shape[:2]

	# clone the output frame, then convert it from BGR to RGB
	# ordering, resize the frame to a fixed 224x224, and then
	# perform mean subtraction
	output = frame.copy()
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	frame = cv2.resize(frame, (224, 224)).astype("float32")
	frame -= mean

	# make predictions on the frame and then update the predictions
	# queue
	preds = model.predict(np.expand_dims(frame, axis=0))[0]
	Q.append(preds)
    
	# perform prediction averaging over the current history of
	# previous predictions
	results = np.array(Q).mean(axis=0)
	i = np.argmax(results)
	label = lb.classes_[i]
	text = "{}".format(label)
	#print(text)
	if "wrestling" in text or "boxing" in text:# in ["boxing", "wrestling"]:		 
		#print("assault detected!")
		#text = "{}".format(label)
		text = "Assault Detected!"
		color = (0, 0, 255)
	else:
		#print("all good!")
		text = "Normal Activity"
		color = (0, 255, 0)

	#write raw images for training
	if training:
		cv2.imwrite(save_frames_to_dir + "%d.jpg" % count, output)
	
	# draw the activity on the output frame
	cv2.putText(output, text, (35, 50), cv2.FONT_HERSHEY_SIMPLEX,
	 	1.25, color, 5)
	#print(count)
	if record_output:# and count < 160:
		# check if the video writer is None
		if writer is None:
		# 	# initialize our video writer
			fourcc = cv2.VideoWriter_fourcc(*"MJPG")
			writer = cv2.VideoWriter(args["output"], fourcc, 30,
				(W, H), True)
	
		# # record the results 
		writer.write(output)

		# # show the output image
		cv2.imshow("Output", output)
	
	# # if the `q` key was pressed, break from the loop
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break

# Compute fps
seconds = time.time() - start
fps  = count / seconds;
print ("Estimated frames per second : {0}".format(fps))

# release the file pointers
print("[INFO] cleaning up...")
if record_output:
	writer.release()
if use_video_as_input:
	vs.release()
