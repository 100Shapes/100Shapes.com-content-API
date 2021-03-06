#!/bin/sh
echo "Injecting Enviroment Variables"
ep /etc/nginx/sites-enabled/nginx.conf

cd /home/app/
echo "Pulling content from branch: ${BRANCH:-master}@${GIT_URL}"
git pull

echo "Running npm install"
cd /home/app/
npm install

echo "Fixing permissions"
chown -R app /home/app/

echo "Done"
