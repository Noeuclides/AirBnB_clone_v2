#!/usr/bin/env bash
# set up web servers for the deployment of web_static
apt-get update -y
apt-get install nginx -y
mkdir /data/
mkdir /data/web_static/
mkdir /data/web_static/releases/
mkdir /data/web_static/shared/
mkdir /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
ln -s /data/web_static/releases/test/ /data/web_static/current
chmod -R 664 /data/ 
server {
    location /hbnb_static {
        alias /data/web_static/current/hbnb_static;
    }
}
service nginx restart


