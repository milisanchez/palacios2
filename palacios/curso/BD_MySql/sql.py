import pymysql
from mysql.connector import Error


class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='alumno',
        )
        self.cursor=self.connection.cursor()
        print("Conexión establecida con éxito !")

    def seleccionar_usuarios(self, id):
        sql = 'SELECT nombre,dni, domicilio, email FROM alumno WHERE id = {}'.format(id)
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            print('Nombre:', user[0])
            print('DNI:', user[1])
            print('Email:', user[2])
        except Exception as e:
            raise

    def seleccionar_todos_usuarios(self):
        sql = 'SELECT nombre,dni, domicilio, email FROM alumno'
        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()
            
            for user in users:
                print('Nombre:', user[0])
                print('DNI:', user[1])
                print('Email:', user[2])
                print('_______\n')

        except Exception as e:
            raise

    def actualizar_usuarios(self, id, username):
        sql = "UPDATE alumno SET username='{}' WHERE id = {}".format(username,id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
        
    def close(self):
        self.connection.close()
        
database=DataBase()
database.seleccionar_usuarios(1)
database.actualizar_usuarios(1,'Marcelo')
database.seleccionar_usuarios(1)
database.close()
