#!/usr/bin/env bash
# install nginx
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
sudo service nginx restart
# create data folder
sudo mkdir -p /data/
# create data/web_static folder
sudo mkdir -p /data/web_static/
# create data/web_static/releases folder
sudo mkdir -p /data/web_static/releases/
# create data/web_static/shared folder
sudo mkdir -p /data/web_static/shared/
# create data/web_static/releases/test folder
sudo mkdir -p /data/web_static/releases/test/
# create fake html file
sudo echo "<html>Holberton School</html" | sudo tee /data/web_static/releases/test/index.html
# create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# give ownership to ubuntu
sudo chown -R ubuntu:ubuntu /data/
# update the nginx config
location="location /hbnb_static {\n\t\talias /data/web_static/current;\n\t}"
sudo sed -i "s@# pass the PHP@$location\n\n\t# pass the PHP@" /etc/nginx/sites-available/default
sudo service nginx restart
