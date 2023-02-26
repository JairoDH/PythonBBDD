import MySQLdb
import sys

#conectarse

try:
        db = MySQLdb.connect("localhost","jairo","1994","empresa" )
except MySQLdb.Error as e:
        print("No se pudo conectar a la base de datos",e)
        sys.exit(1)
print("Conectado")


def menu():
    print("Menu: ")
    print("1. Mostrar trabajadores. ")
    print("2. Consultar trabajador por su teléfono. ")
    print("3. Mostrar trabajadores asociados por matrícula. ")
    print("4. Introducir camión nuevo a la empresa: ")
    print("5. Eliminar camión.")
    print("6. Actualización de los datos del trabajador.")
    print("7. Salir")
    opcion = int(input("Selecciona una opcion: "))
    return opcion

#consultanumero1
def mostrar_trabajadores():
       
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

def informacion_telefono():
    
    codigo = int(input("Introduzca el código del trabajador: "))

    sql = "SELECT * FROM CONDUCTOR WHERE codigo = %s"
    cursor = db.cursor()

    try:     
        cursor.execute(sql, codigo)
        registro = cursor.fetchone()
        while resultado:
            print(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5],registro[6],registro[7],registro[8],registro[9])
            resultado = cursor.fetchone()
    except:
        print("Error en la consulta")
    db.close()
    return 

#consultanumero3

def informacion_matricula():

    matricula_camion = input("Introduzca la matrícula del camión: ")

    sql = "SELECT * FROM CAMION_CONDUCTOR cc JOIN CONDUCTOR c ON cc.codigo_conductor = c.codigo JOIN CAMION ca ON cc.matricula_camion = ca.matricula WHERE ca.matricula = %s"
    cursor = db.cursor()

    try:
        cursor.execute(sql, matricula_camion)
        registro = cursor.fetchone()
        while resultado:
            print(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5],registro[6],registro[7],registro[8],registro[9])
            resultado = cursor.fetchone()
    except:
        print("Error en la consulta")
    db.close()

#consultanumero4

def nuevo_camion():

    matri = input("Introduce la matrícula (AAAA000): ")
    fecha = input("Introduce la fecha de alta (YYYY-MM-DD): ")
    peso = int(input("Introduce el peso máximo a transportar: "))

    sql = "INSERT INTO CAMION (matricula, fecha_alta, peso_maximo) VALUES ('{matri}', '{fecha}', {peso})"
    cursor = db.cursor()

    try:
        cursor.execute(sql,matri,fecha,peso)
        db.commit()
    except:
        db.rollback()
    db.close()

#consultanumero5

def eliminar_camion():

    dni = input("Introduce el DNI: ")


    sql = "SELECT matricula_camion FROM CAMION_CONDUCTOR WHERE codigo_conductor = ( SELECT codigo FROM CONDUCTOR where DNI = '{dni}')"
    cursor = db.cursor()

    try:
        cursor.execute(sql, dni)
        resultado = cursor.fetchone()
        if resultado is not None:
            matricula_camion = resultado[0]
            borrar = "DELETE FROM CAMION WHERE matricula = '{matricula_camion}"
            cursor.execute(sql, matricula_camion, borrar)
            db.commit()
            print("Camión con matrícula {matricula_camion} se ha eliminado correctamente.")
    except:
            db.rollback()
            print("No hay camión asignado al DNI {dni}.")
    db.close()

#consultanumero6

def actualizar_trabajador():

    nombre = input("Dime el nombre del conductor: ")
    apellido1 = input("Dime el primer apellido del conductor: ")

    nuevo_telefono = input("Introduce el número de teléfono: ")
    nuevo_municipio = input("Introduce el nuevo municipio: ")


    sql = "UPDATE CONDUCTOR SET telefono = '{nuevo_telefono}', poblacion = '{nuevo_municipio}' WHERE nombre = '{nombre}' AND apellido1 = '{apellido1}'"
    cursor = cursor.db()

    try:
        cursor.execute(sql,nombre,apellido1,nuevo_telefono,nuevo_municipio)
        if cursor.rowcount == 0:
            print("No se ha encontrado conductor con el nombre {nombre} {apellido1}.")
    except:
            db.commit()
            print("Se ha actualizado correctamente el conductor {nombre} {apellido1}.")
    db.close()