#!/usr/bin/bash 

sed -i 's/\[]/\["3.84.7.210"]/' /home/ubuntu/blogprojectdrf-2/main/settings.py
python  manage.py makemigrations
sudo systemctl restart gunicorn
sudo systemctl restart nginx
