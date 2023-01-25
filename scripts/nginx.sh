#!/usr/bin/bash

sudo systemctl daemon-reload
systemctl restart gunicorn.service
sudo cp /nginx/nginx.conf /etc/nginx/sites-available/ci-cd-django
sudo ln -s /etc/nginx/sites-available/ci-cd-django /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
sudo ufw delete allow 8000
sudo ufw allow 'Nginx Full'