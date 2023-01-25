#!/usr/bin/bash 

sed -i 's/\[]/\["54.144.250.113"]/' /home/ubuntu/blogprojectdrf/blog/settings.py

sudo service gunicorn restart
sudo service nginx restart


