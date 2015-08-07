#!/bin/sh
echo "Clearing old Content"
rm -r home/app/content
echo "Pulling content from branch: ${BRANCH:-master}@${GIT_URL}"
git clone --depth 1 -b ${BRANCH:-master} ${GIT_URL}  /tmp/app
echo "Transfering content"
cp -r /tmp/app/* /home/app/
echo "Tidying temp content"
rm -r /tmp/app
cd /home/app/
echo "Content Pulled. Running npm install"
npm install
echo "npm install complete. Fixing permissions"
chown -R app /home/app/
