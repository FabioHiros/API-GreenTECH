USE dadosensores;

CREATE TABLE estufa(
    datahora DATETIME PRIMARY KEY NOT NULL,
    umidade_solo INT,
    umidade_ambiente INT,
    temperatura DECIMAL(7,1),
    volume_agua DECIMAL(9,2)
);