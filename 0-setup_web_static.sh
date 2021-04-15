#!/usr/bin/env bash
# set up web server for webstatic deployment
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo printf '%s\n' \
'<html>' \
'  <head>' \
'  </head>' \
'  <body>' \
'     Holberton School' \
'  </body>' \
'</html>' \
|sudo tee /data/web_static/releases/test/index.html
sudo ln -fsn /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

location='location /hbnb_static/ { alias /data/web_static/current/; autoindex off; }'
sudo sed -i "/listen \[::\]:80 default_server;/a $location" /etc/nginx/sites-enabled/default
sudo service nginx restart
