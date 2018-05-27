#!/bin/bash

cd /
cd /home/pi/meteo-api
sudo flask/bin/python app.py &
sudo java -jar  -Xmx64m -XX:+UseConcMarkSweepGC -jamvm  meteoProcessStandalone.jar &
