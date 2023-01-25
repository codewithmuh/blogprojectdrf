#!/usr/bin/bash 

sed -i 's/\[]/\["54.144.250.113"]/' /home/ubuntu/blogprojectdrf/blog/settings.py

sudo service gunicorn restart
sudo fuser -k 80/tcp
sudo fuser -k 443/tcp
sudo systemctl start nginx
sudo systemctl reload nginx
sudo nginx -t
sudo systemctl restart nginx
sudo nginx -t
sudo service nginx restart
sudo tail -f /var/log/nginx/error.log


