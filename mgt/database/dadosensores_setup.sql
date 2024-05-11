-- Active: 1715455220432@@127.0.0.1@3306@information_schema
CREATE DATABASE dadosensores;

USE dadosensores;

CREATE TABLE estufa(
    datahora DATETIME PRIMARY KEY NOT NULL,
    umidade_solo INT,
    umidade_ambiente INT,
    temperatura DECIMAL(7,1),
    volume_agua DECIMAL(9,2)
);

CREATE USER 'estufa'@'localhost' IDENTIFIED BY 'estufa';
GRANT ALL PRIVILEGES ON dadosensores.* TO 'estufa'@'localhost' WITH GRANT OPTION;
REVOKE DROP, ALTER ON dadosensores.* FROM 'estufa'@'localhost';
FLUSH PRIVILEGES;