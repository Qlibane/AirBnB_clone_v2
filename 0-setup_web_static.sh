#!/usr/bin/env bash
#Bash script to set up web servers for the deployment of web_static
if ! command -v nginx > /dev/null
then
        sudo apt -y update
        sudo apt-get -y upgrade
        sudo apt-get -y install nginx
fi
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
if [ ! -e /data/web_static/releases/test/index.html ]
then
        touch /data/web_static/releases/test/index.html
fi
echo "Simple content to test nginx configuration" > /data/web_static/releases/test/index.html
if [ -e /data/web_static/current ]
then
        rm /data/web_static/current
fi
ln -s /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
sudo sed -i "/server_name _;/a \\
        location /hbnb_static { \\
                alias /data/web_static/current/; \\
        }" /etc/nginx/sites-available/default
sudo service nginx restart

