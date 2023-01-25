#!/usr/bin/bash
sudo cp /home/ubuntu/blogprojectdrf/gunicorn/gunicorn.socket  /etc/systemd/system/gunicorn.socket
sudo cp /home/ubuntu/blogprojectdrf/gunicorn/gunicorn.service  /etc/systemd/system/gunicorn.service

sudo systemctl start gunicorn
sudo systemctl enable gunicorn
