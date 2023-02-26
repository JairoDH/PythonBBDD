from funcionesbbdd import *
import MySQLdb
import sys

try:
        db = MySQLdb.connect("localhost","jairo","1994","empresa" )
        
except MySQLdb.Error as e:
        print("No se pudo conectar a la base de datos",e)
        sys.exit(1)
print("Conectado")

opcion = menu()
print (opcion)
while opcion != 7 : 
    if opcion == 1 :
        mostrar_trabajadores
    elif opcion == 2:
        informacion_telefono
    elif opcion == 3:
        informacion_matricula
    elif opcion == 4:
        nuevo_camion
    elif opcion == 5:
        actualizar_trabajador
    elif opcion == 6:
        opcion = menu()
