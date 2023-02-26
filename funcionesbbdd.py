import sys 
import MySQLdb

#conectarse

try:
        db = MySQLdb.connect("localhost","jairo","1994","empresa" )
except MySQLdb.Error as e:
        print("No se pudo conectar a la base de datos",e)
        sys.exit(1)
print("Conectado")

#consultanumero1

sql = "select c.nombre, c.apellido1, c.provincia, ca.matricula from CAMION_CONDUCTOR cc JOIN CONDUCTOR c ON cc.codigo_conductor = c.codigo JOIN CAMION ca ON cc.matricula_camion = ca.matricula"
cursor = db.cursor()
try:
    cursor.execute(sql)
    registros = cursor.fetchall()
    for registro in registros:
           print(registro[0],registros[1],registros[2],registro[3])
except:
       print("Error en la consulta")
db.close()

#consultanumero2

try:
        db = MySQLdb.connect("localhost","jairo","1994","empresa" )
except MySQLdb.Error as e:
        print("No se pudo conectar a la base de datos",e)
        sys.exit(1)
print("Conectado")

codigotrabajador = int(input("Introduzca el código del trabajador: "))


sql = "SELECT * FROM CONDUCTOR WHERE codigo = %s"
cursor = db.cursor()

try:     
    cursor.execute(sql)
    resultado = cursor.fetchone()
    while resultado:
           print(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5],registro[6],registro[7],registro[8],registro[9])
           resultado = cursor.fetchone()
except:
       print("Error en la consulta")
db.close()

#consultanumero3

try:
        db = MySQLdb.connect("localhost","jairo","1994","empresa" )
except MySQLdb.Error as e:
        print("No se pudo conectar a la base de datos",e)
        sys.exit(1)
print("Conectado")

matricula_camion = input("Introduzca la matrícula del camión: ")

sql = "SELECT * FROM CAMION_CONDUCTOR cc JOIN CONDUCTOR c ON cc.codigo_conductor = c.codigo JOIN CAMION ca ON cc.matricula_camion = ca.matricula WHERE ca.matricula = %s"
cursor = db.cursor()

try:
    cursor.execute(sql)
    resultado = cursor.fetchone()
    while resultado:
           print(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5],registro[6],registro[7],registro[8],registro[9])
           resultado = cursor.fetchone()
except:
       print("Error en la consulta")
db.close()

#consultanumero4

try:
        db = MySQLdb.connect("localhost","jairo","1994","empresa" )
except MySQLdb.Error as e:
        print("No se pudo conectar a la base de datos",e)
        sys.exit(1)
print("Conectado")

matri = input("Introduce la matrícula (AAAA000): ")
fecha = input("Introduce la fecha de alta (YYYY-MM-DD): ")
peso = int(input("Introduce el peso máximo a transportar: "))

sql = "INSERT INTO CAMION (matricula, fecha_alta, peso_maximo) VALUES ('{matri}', '{fecha}', {peso})"
cursor = db.cursor()

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()

#consultanumero5

try:
        db = MySQLdb.connect("localhost","jairo","1994","empresa" )
except MySQLdb.Error as e:
        print("No se pudo conectar a la base de datos",e)
        sys.exit(1)
print("Conectado")

dni = input("Introduce el DNI: ")

cursor = db.cursor()
sql = "SELECT matricula_camion FROM CAMION_CONDUCTOR WHERE codigo_conductor = ( SELECT codigo FROM CONDUCTOR where DNI = '{dni}')"

try:
    cursor.execute(sql)
    resultado = cursor.fetchone()
    if resultado is not None:
           matricula_camion = resultado[0]
           borrar = "DELETE FROM CAMION WHERE matricula = '{matricula_camion}"
           cursor.execute(sql)
           db.commit()
           print("Camión con matrícula {matricula_camion} se ha eliminado correctamente.")
except:
        db.rollback()
        print("No hay camión asignado al DNI {dni}.")
db.close()

