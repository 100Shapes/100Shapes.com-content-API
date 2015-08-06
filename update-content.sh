#!/bin/sh
echo "Clearing old Content from branch: ${BRANCH:-master}@${GIT_URL}"
rm -r home/app/content
git clone --depth 1 -b ${BRANCH:-master} ${GIT_URL}  /tmp/app
cp -r /tmp/app/* /home/app/
rm -r /tmp/app
cd /home/app/
echo "Content Pulled. Running npm install"
npm install
echo "npm install complete. Tidying up"
chown -R app /home/app/
