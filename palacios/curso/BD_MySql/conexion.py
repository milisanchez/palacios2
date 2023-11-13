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
        infoServer = conexion.get_server_info()
        print("Info del servidor: ", infoServer)
except Error as ex:
    print("Error durante la conexión", ex)
finally:
    if conexion.is_connected():
        conexion.close()
        print("La conexión ha finalizado.")