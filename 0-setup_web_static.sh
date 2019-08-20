#!/usr/bin/env bash
# set up web servers for the deployment of web_static
if [ ! -x /usr/sbin/nginx ];then
    apt-get update -y
    apt-get install nginx -y
fi
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
ln -snf /data/web_static/releases/test/ /data/web_static/current 
sudo chown -R ubuntu:ubuntu /data 
sed -i '37a\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/hbnb_static;\n\t}' /etc/nginx/sites-enabled/default
service nginx restart
