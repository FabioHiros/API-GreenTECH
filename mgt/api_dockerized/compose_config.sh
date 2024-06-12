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
    image: ericfatec/greentechcompose:latest
    links:
      - db
    ports:
      - "5000:5000"
  db:
    image: mysql:latest
    ports:
      - "3306:3306"
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: dadosensores
      MYSQL_USER: estufa
      MYSQL_PASSWORD: estufa
    volumes:
      - ./db/:/docker-entrypoint-initdb.d/
EOF

cat <<EOF > /home/ubuntu/dockerize/db/init.sql
USE dadosensores;

CREATE TABLE estufa(
    datahora DATETIME PRIMARY KEY NOT NULL,
    umidade_solo INT,
    umidade_ambiente INT,
    temperatura DECIMAL(7,1),
    volume_agua DECIMAL(9,2)
);
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