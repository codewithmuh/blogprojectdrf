#!/usr/bin/bash

sudo cp /blogprojectdrf/gunicorn/gunicorn.service  /etc/systemd/system/gunicorn.service

sudo systemctl start gunicorn
sudo systemctl enable gunicorn