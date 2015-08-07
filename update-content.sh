#!/bin/sh
echo "Injecting Enviroment Variables"
# ep /etc/nginx/sites-enabled/nginx.conf
ep /etc/my_init.d/update-content.sh

if [ $1 = "fresh" ]; then
    echo "Doing fresh clone"
    rm -r /home/app
    echo "Cloning content from branch: ${BRANCH:-master}@${GIT_URL}"
    git clone --depth 1 -b ${BRANCH:-master} ${GIT_URL} /home/app
else
    cd /home/app/
    echo "Pulling content from branch: ${BRANCH:-master}@${GIT_URL}"
    git pull
fi

echo "Running npm install"
cd /home/app/
npm install

# echo "Running webpack"
# webpack -p

echo "Fixing permissions"
chown -R app /home/app/
