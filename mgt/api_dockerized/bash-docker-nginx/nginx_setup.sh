#!/bin/bash

apt-get update
apt-get install -y nginx

NGINX_CONF='upstream greentech {
    server 18.208.72.123:5000;
    server 100.27.173.200:5000;
    server 34.234.112.100:5000;
}
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;

    server_name _;

    location / {
        proxy_pass http://greentech;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}'

echo "$NGINX_CONF" | sudo tee /etc/nginx/sites-available/default

nginx -t

systemctl reload nginx

systemctl enable nginx

systemctl start nginx

systemctl status nginx