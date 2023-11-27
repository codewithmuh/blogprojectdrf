#!/usr/bin/env bash

sudo chown -R ubuntu:ubuntu ~/financetracker
virtualenv /home/ubuntu/financetracker/venv
source /home/ubuntu/financetracker/venv/bin/activate
pip install -r /home/ubuntu/financetracker/requirements.txt