use salones_vacios;

CREATE TABLE salones(
	id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(5)
);

CREATE TABLE clases(
	id_salon BIGINT UNSIGNED,
    dia VARCHAR(20),
    hora_inicio TIME,
    hora_fin TIME,
    PRIMARY KEY(id_salon,dia,hora_inicio,hora_fin),
    FOREIGN KEY (id_salon) REFERENCES salones(id)
);

INSERT INTO salones values(0,"A701");
INSERT INTO salones (nombre) values("A702");

SELECT * FROM salones;

INSERT INTO clases VALUES(1,"lunes","08:00:00","10:00:00");
INSERT INTO clases VALUES(1,"lunes","11:00:00","13:00:00");
INSERT INTO clases VALUES(1,"lunes","14:00:00","16:00:00");
INSERT INTO clases VALUES(1,"lunes","16:00:00","18:00:00");
INSERT INTO clases VALUES(1,"lunes","18:00:00","20:00:00");

SELECT * FROM clases;

SELECT s.id, s.nombre
FROM salones s
LEFT JOIN clases c ON s.id = c.id_salon
                   AND c.dia = 'lunes'  -- Reemplaza con el día deseado
                   AND c.hora_inicio <= '10:00:00'  -- Hora de inicio deseada
                   AND c.hora_fin >= '11:00:00'  -- Hora de fin deseada
WHERE c.id_salon IS NULL;

INSERT INTO clases VALUES(2,"lunes","16:00:00","18:00:00");
INSERT INTO clases VALUES(2,"lunes","11:00:00","13:00:00");
INSERT INTO clases VALUES(2,"lunes","20:00:00","22:00:00");

DELETE FROM clases
WHERE id_salon=2 AND dia="lunes" AND hora_inicio="16:00:00" AND hora_fin="18:00:00";

SELECT * FROM clases;

