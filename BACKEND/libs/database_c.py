import os
import psycopg2
from flask import make_response
from dotenv import load_dotenv


class database_c():

    # Cargar datos de .env
    load_dotenv()

    # Variables Recursivas
    conexion = None
    db = None
    DATABASE_URL = os.environ.get('POSTGRES_URL')

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
            
            self.conexion = psycopg2.connect(self.DATABASE_URL)

            self.db = self.conexion.cursor()

        except Exception as e:
            print(f"Error al conectar a la base de datos: {str(e)}")

    # Desconectar de la DB
    def desconectar_db(self):

        #Commit
        self.conexion.commit()

        #Cerrar Cursor Y DB
        self.db.close()
        self.conexion.close()

    # Guardar Actividades Logs
    def logs(self,consulta,accion):

        try:
            self.conectar_db()  # Se conecta a la DB

            # Usa una consulta preparada con parámetros
            self.db.execute("INSERT INTO Logs (consulta, accion) VALUES (%s, %s)", (consulta, accion))

            self.desconectar_db()  # Se desconecta de la DB

        except Exception as e:
            print(e)

    # Manipular Database
    def control_db(self,consulta): #Realizar Consulta
        
        try:
            self.conectar_db() #Se Conecta A La DB
            
            self.db.execute(consulta) #Se Realiza La Busqueda Personalizada
            
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