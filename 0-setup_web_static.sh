#!/usr/bin/env bash
#Script
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test/
echo "\
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
var="\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t\tautoindex off;\n\t}"
sed -i "29 i\\
$var" /etc/nginx/sites-available/default
service nginx restart
