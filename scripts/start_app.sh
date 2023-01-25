#!/usr/bin/bash 

sed -i 's/\[]/\["54.144.250.113"]/' /home/ubuntu/blogprojectdrf/blog/settings.py

sudo service gunicorn restart
sudo fuser -k 80/tcp
sudo fuser -k 443/tcp
sudo service nginx restart


