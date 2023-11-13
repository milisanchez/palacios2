import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password="",
        db='condominio',
    )

    if conexion.is_connected():
        print("Conexión exitosa. ")
        cursor=conexion.cursor()
        administrador = input("Ingrese nombre de administrador: ")
        sentencia="INSERT INTO tipousuario (administrador) VALUES ('{0}')".format(administrador)
        cursor.execute(sentencia)
        conexion.commit()
        print("Registro insertado con éxito. ")
except Error as ex:
    print("Error durante la conexión", ex)
finally:
    if conexion.is_connected():
        conexion.close()
        print("La conexión ha finalizado.")