#!/bin/bash
sudo apt-get update
sudo apt-get -y install python3 python3-pip git
git clone https://github.com/Proweex/sintaksys-api.git
cd sintaksys-api
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
nohup gunicorn -w 5 -b 0.0.0.0:8080 app:app > $HOME/api-call-log.txt 2>&1