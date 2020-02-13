#!/bin/bash

# kill the bash process so the app doesn't keep restarting. 
ps -elf | grep run_app.sh | awk '{print $4}' | xargs kill 

# kill the app python processes 
ps -elf | grep predict_camera.py | awk '{print $4}' | xargs kill 

exit 0
