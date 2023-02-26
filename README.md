
# PythonBBDD
Realizar tres programas, uno para cada BBDD ( Oracle, Mariadb y Postgres) con Python.


# Mostrar los trabajadores con su provincia y los camiones asignados.

# Pedir número del trabajador y mostrar toda su información. 

# Mostrar los datos de los trabajadores pidiendo la matricula del camion.

# inserción de datos de un nuevo camión pidiendo la matricula, fecha de alta y peso máximo.

# Pedir DNI del conductor para eliminar el camión.

# pedir nombre del trabajador para actualizar el número telefono y el municipio.


Las tablas seleccionadas de la base de datos: 


CREATE TABLE CAMION(
    matricula varchar(7),
    fecha_alta date NOT NULL,
    peso_maximo float(7,2) 
);

CREATE TABLE CONDUCTOR(
    codigo int(5),
    nombre varchar(20),
    apellido1 varchar(20),
    apellido2 varchar(20),
    DNI varchar(9) NOT NULL,
    calle varchar(20),
    nº_calle int(5),
    provincia varchar(10),
    poblacion varchar(10),
    telefono varchar(9) NOT NULL
);

CREATE TABLE CAMION_CONDUCTOR(
    matricula_camion varchar(7),
    codigo_conductor int(5),
    fecha date NOT NULL
);
