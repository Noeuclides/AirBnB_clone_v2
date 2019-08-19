#!/usr/bin/env bash
# set up web servers for the deployment of web_static
apt-get update -y
apt-get install nginx -y
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
rm /data/web_static/current 
ln -s /data/web_static/releases/test/ /data/web_static/current 
sudo chown -R ubuntu:ubuntu /data 
sed -i '37a\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/hbnb_static;\n\t}' /etc/nginx/sites-enabled/default
service nginx restart
