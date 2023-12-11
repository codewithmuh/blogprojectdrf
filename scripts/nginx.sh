
#!/usr/bin/bash

sudo systemctl daemon-reload
sudo rm -f /etc/nginx/sites-enabled/default

sudo cp /home/ubuntu/Project_folder_name/nginx/nginx.conf /etc/nginx/sites-available/fodler_name_where_seetngs.py_is
sudo ln -s /etc/nginx/sites-available/fodler_name_where_seetngs.py_is /etc/nginx/sites-enabled/
#sudo ln -s /etc/nginx/sites-available/blog /etc/nginx/sites-enabled
#sudo nginx -t
sudo gpasswd -a www-data ubuntu
sudo systemctl restart nginx

