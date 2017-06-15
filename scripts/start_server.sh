#!/bin/bash
cd /home/ec2-user/devop/
source ./bin/activate
cd HelloDevOp/
python manage.py runserver 0.0.0.0:8000
