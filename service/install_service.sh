#!/bin/bash

# Get the base directory of the underquad repo
base_dir=`realpath $0 | xargs dirname | xargs dirname`

# Write out the systemd service file
echo "
[Unit]
Description=AIDR App
Requires=multi-user.target rc.local.service
After=multi-user.target rc.local.service

[Service]
Type=simple
WorkingDirectory=$base_dir
ExecStart=$base_dir/service/run_app.sh
ExecStop=$base_dir/service/stop_app.sh


[Install]
WantedBy=aidr_app.target
" | sudo tee /lib/systemd/system/aidr_app.service

# Write out the systemd target file
echo "
[Unit]
Description=AIDR Target
Requires=multi-user.target rc.local.service
After=multi-user.target rc.local.service
Conflicts=rescue.target
AllowIsolate=yes
" | sudo tee /lib/systemd/system/aidr_app.target

# Make the graphical target require underquad target. The default target 
# on Raspian is graphical target so this ensures services targeting 
# underquad target are started on boot as well.
sudo sed -i -e "s/\(Requires.*\)/\1 aidr_app.target/g" /lib/systemd/system/graphical.target

# Enable and start the service
sudo systemctl daemon-reload
sudo systemctl enable aidr_app
sudo systemctl start aidr_app
