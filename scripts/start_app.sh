#!/usr/bin/bash 

sed -i 's/\[]/\["54.144.250.113"]/' /home/ubuntu/blogprojectdrf/blog/settings.py

sudo service gunicorn restart
sudo systemctl reload nginx
sudo nginx -t
sudo systemctl restart nginx
sudo nginx -t
sudo service nginx restart
sudo systemctl status nginx
sudo tail -f /var/log/nginx/error.log