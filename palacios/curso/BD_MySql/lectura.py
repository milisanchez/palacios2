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
        cursor.execute("SELECT database();")
        registro=cursor.fetchone()
        print("Conectado a la BD: ", registro)
        cursor.execute("SELECT * FROM tipousuario")
        resultados=cursor.fetchall()
        for fila in resultados:
            print(fila[0], fila[1], fila[2], fila[3])
            print("Total de registros: ", cursor.column_names)
except Error as ex:
    print("Error durante la conexión", ex)
finally:
    if conexion.is_connected():
        conexion.close()
        print("La conexión ha finalizado.")