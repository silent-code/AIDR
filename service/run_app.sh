#!/bin/bash

# Loop indefinitely, restarting the app if it exits.
while true; do
	# Kill any orphaned app python processes that might be running.
	ps -elf | grep main.py | awk '{print $4}' | xargs kill 
	workon deeplearning
	python ./python predict_camera.py --model model/activity.model --input example_clips/assault.mp4 --label-bin model/lb.pickle --output output/assault.avi --size 100

done
