#!/bin/sh
git clone https://github.com/100Shapes/100Shapes.com-content-API.git /tmp/app
cp -r /tmp/app/* /home/app/
rm -r /tmp/app
cd /home/app/
npm install
chown -R app /home/app/
