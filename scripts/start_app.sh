#!/usr/bin/bash 

sed -i 's/\[]/\["54.144.250.113"]/' /home/ubuntu/blogprojectdrf/main/settings.py
python  manage.py makemigrations
sudo systemctl restart gunicorn
sudo systemctl restart nginx
