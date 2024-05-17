import os
import pymysql
from flask import make_response
from dotenv import load_dotenv


class database_c():

    # Cargar datos de .env
    load_dotenv()

    # Variables Recursivas
    conexion = None
    db = None
    codigo = os.getenv("OTP")
    puerto = int(os.getenv("DATABASE_PORT"))

    # Retorno De Mensajes
    def message_return(self, text, status_code):
        # Se crea el mensaje
        message = make_response(text)

        # Se asigna el status code
        message.status_code = status_code

        # Se retorna el mensaje
        return message

    # Conectarse a la DB
    def conectar_db(self):
        try:
            self.conexion = pymysql.connect(
            host=os.getenv("DATABASE_HOST"),
            user=os.getenv("DATABASE_USER"),
            passwd=os.getenv("DATABASE_PASSWORD"),
            db=os.getenv("DATABASE_NAME"),
            port=self.puerto,
            autocommit=True,
            ssl={ "rejecUnauthorized": False }
        )
            self.db = self.conexion.cursor()

        except Exception as e:
            print(f"Error al conectar a la base de datos: {str(e)}")

    # Desconectar de la DB
    def desconectar_db(self):

        #Cerrar Cursor Y DB
        self.db.close()
        self.conexion.close()

    # Guardar Actividades Logs
    def logs(self,consulta,accion):

        try:
            self.conectar_db() #Se Conecta A La DB

            self.db.execute(""" INSERT INTO Logs (consulta,accion) VALUES ("{}","{}") """.format(consulta,accion))

            self.desconectar_db() #Se Desconecta De La DB

        except Exception as e:
            print(e)

    # Manipular Database
    def control_db(self,consulta): #Realizar Consulta
        try:
            self.conectar_db() #Se Conecta A La DB
            
            self.db.execute("""{};""".format(consulta)) #Se Realiza La Busqueda Personalizada

            if "SELECT" in consulta:

                data = self.db.fetchall() #Se Guardan

                self.desconectar_db() #Se Desconecta De La DB

                return data

            elif "INSERT" in consulta:

                data = self.db.lastrowid

                self.desconectar_db() #Se Desconecta De La DB

                return data
            
            else:

                data = self.db.fetchall() #Se Guardan

                self.desconectar_db() #Se Desconecta De La DB

                return data

        except Exception as e:
            print(e)

database_api = database_c()

#from star_lumiere.star_lumire import api_star_lumiere


""" # MOVER POR SEPARADO AGREGAR CATEGORIAS
resp = api_star_lumiere.view_categories()

database_api.conectar_db()

for x in resp:
    database_api.db.execute("INSERT INTO C_Service (id_c_plataform,name) VALUES ('1','{}')".format(x))

database_api.desconectar_db()
# UP
 """


""" #MOVER POR SEPARADO AGREGAR ID SERVICIOS
database_api.conectar_db()

resp = api_star_lumiere.view_services()

database_api.db.execute("SELECT * FROM C_Service")

resp_1 = database_api.db.fetchall()

for x in resp:
    for y in resp_1:
        if x['category'] == y[2]:
            database_api.db.execute("INSERT INTO Service (id_original,id_c_service) VALUES ('{}','{}')".format(x['service'],y[0]))
            pass
        else:
            pass
#UP """
