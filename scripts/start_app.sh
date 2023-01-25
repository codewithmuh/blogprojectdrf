#!/usr/bin/bash 

sed -i 's/\[]/\["54.144.250.113"]/' /home/ubuntu/blogprojectdrf/blog/settings.py


sudo systemctl restart gunicorn
sudo systemctl status gunicorn
sudo service gunicorn restart
sudo service nginx restart

#sudo systemctl reload nginx
#sudo tail -f /var/log/nginx/error.log
#sudo nginx -t
# Check the status
#systemctl status gunicorn
# Restart:
#systemctl restart gunicorn
#sudo systemctl status nginx
