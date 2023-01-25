#!/usr/bin/bash

sudo cp /gunicorn/gunicorn.service  /etc/systemd/system/gunicorn.service
sudo systemctl start gunicorn
sudo systemctl enable gunicorn