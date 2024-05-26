#!/bin/bash

apt update

apt install docker.io -y
apt install docker-compose-v2 -y

usermod -aG docker ubuntu

service docker restart

mkdir -p /home/ubuntu/dockerize/db

cat <<EOF > /home/ubuntu/dockerize/docker-compose.yml
version: "3.3"
services:
  app:
    image: ericfatec/apigreentech:latest
    ports:
      - "5000:8000"
EOF

chown -R ubuntu:ubuntu /home/ubuntu/dockerize

bash -c 'cat <<EOF > /etc/systemd/system/docker-compose-app.service
[Unit]
Description=Docker Compose Application Service
Requires=docker.service
After=docker.service

[Service]
WorkingDirectory=/home/ubuntu/dockerize
ExecStart=/usr/bin/docker compose up
ExecStop=/usr/bin/docker compose down
Restart=always
User=ubuntu

[Install]
WantedBy=multi-user.target
EOF'

systemctl daemon-reload
systemctl enable docker-compose-app.service

systemctl start docker-compose-app.service

echo "Setup complete. Docker and Docker Compose are installed, and the service is set to start on boot."