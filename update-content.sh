#!/bin/sh
echo "Clearing old Content"
rm -r home/app/content
git clone -b ${BRANCH:-master} https://github.com/100Shapes/100Shapes.com-content-API.git /tmp/app
cp -r /tmp/app/* /home/app/
rm -r /tmp/app
cd /home/app/
echo "Content Pulled. Running npm install"
npm install
echo "npm install complete. Tidying up"
chown -R app /home/app/
