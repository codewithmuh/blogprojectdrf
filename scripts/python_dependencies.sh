#!/usr/bin/env bash

sudo chown -R ubuntu:ubuntu ~/Project_folder_name
virtualenv /home/ubuntu/Project_folder_name/venv
source /home/ubuntu/Project_folder_name/venv/bin/activate
pip install -r /home/ubuntu/Project_folder_name/requirements.txt