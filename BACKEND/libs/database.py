import pyotp
from flask import make_response
from dotenv import load_dotenv
import os
import pymysql

class database_c():

    #Cargar Datos De .env
    load_dotenv()

    #Variables Recursiva
    conexion = None
    db = None
    codigo = os.getenv("OTP")

    #Retorno De Mensajes
    def message_return(self,text,status_code):

        #Se Crea El Mensaje
        message = make_response(text)

        #Se Asigna El Satus Code
        message.status_code = status_code

        #Se Retorna El Mensaje
        return message

    #Conectarse A La DB
    def conectar_db(self):

        #Crear Conexion
        self.conexion = pymysql.connect(
            #Host, Username, Password, Name DB, AutoCommit, AUTH.
            host=os.getenv("DATABASE_HOST"),
            user=os.getenv("DATABASE_USERNAME"),
            passwd=os.getenv("DATABASE_PASSWORD"),
            db=os.getenv("DATABASE"),
            autocommit=True,
            ssl={ "rejecUnauthorized": False }
        )

        #Crear Cursor
        self.db = self.conexion.cursor()
    
    #Inicializar La DB Si Es Que No Existe
    def inicializar_db(self):

        #Conectarse DB
        self.conectar_db()

        #Crear Logs
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS Logs(
                log_text VARCHAR (1024) NOT NULL
            )
        """)

        #Desconectar DB
        self.desconectar_DB

        #Retorna Que Se Inicializo Bien La DB
        return "DB Users And Admins Inicializado Correctamente"

    #Desconecarse De La DB
    def desconectar_DB(self):

        #Cerrar Cursor Y DB
        self.db.close()
        self.conexion.close()

    #Certificar Codigo OTP Para Usar Funciones
    def code_rol_validation(self, current_password):

        #Si La Contraseña No Se Envia Retorna Falso
        if current_password == None:
            return self.message_return("{'message':'False'}",401)

        #Si La Contraseña Es Una Cadena Vacia Retorna Falso
        if not current_password:
            return self.message_return("{'message':'False'}",401)

        #Si La Contraseña Es De Caracter Valido Se Genera El TOTP
        totp = pyotp.TOTP(self.codigo)

        #Si La Contraseña Es Correcta En Tiempo Real Se Retorna True
        if totp.verify(current_password):
            return self.message_return("{'message':'True'}",200)

        #Si No Coincide Se Retorna False
        return self.message_return("{'message':'False'}",401)

    #Realizar Consultas
    def consult_db(self, consult):

        #Se Conecta A La DB
        self.conectar_db()

        #Se Realiza La Consulta Con La Insercion De Texto
        self.db.execute(f"""
            {consult}
        """)

        #Se Almacena El Resultado
        resp = self.db.fetchall()

        #Se Desconecta De La DB
        self.desconectar_DB()

        #Se Retorna El Mensaje Junto A Codigo 200
        return self.message_return(str(resp),200)

    #Guardar Errores
    def save_logs(self,text):

        #Se Conecta A La DB
        self.conectar_db()
        
        #Se Inserta El Log En La DB
        query = "INSERT INTO Logs (log_text) VALUES (%s)"
        self.db.execute(query, (text,))

        #Se Desconecta De La DB
        self.desconectar_DB()

database = database_c()