import sqlite3
from flask import make_response
from dotenv import load_dotenv
import os
import MySQLdb

class orders_receipt_db():

    #Variables Recursiva
    conexion = None
    db = None

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

        #Cargar Datos De .env
        load_dotenv()

        #Crear Conexion
        self.conexion = MySQLdb.connect(
            #Host, Username, Password, Name DB, AutoCommit, AUTH.
            host=os.getenv("DATABASE_HOST"),
            user=os.getenv("DATABASE_USERNAME"),
            passwd=os.getenv("DATABASE_PASSWORD"),
            db=os.getenv("DATABASE"),
            autocommit=True,
            ssl_mode="VERIFY_IDENTITY",
            ssl={ "rejecUnauthorized": False }
        )

        #Crear Cursor
        self.db = self.conexion.cursor()

    #Desconecarse De La DB
    def desconectar_DB(self):

        #Cerrar Cursor Y DB
        self.db.close()
        self.conexion.close()

    #Inicializar DB
    def inicializar_db(self):

        #Conectar A La DB
        self.conectar_db()

        #Crear Tabla Category Plataform Si Es Que No Existe
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS C_Plataform(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(255) NOT NULL
        )""")

        #Crear Tabla Category Services Si Es Que No Existe
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS C_Service(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                id_c_plataform INTEGER NOT NULL,
                name VARCHAR(255) NOT NULL
        )""")

        #Crear Tabla Servicios Si Es Que No Existe
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS Service(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                id_original INTEGER NOT NULL,
                id_c_service INTEGER NOT NULL,
                name VARCHAR(255) NOT NULL,
                description VARCHAR(255),
                type VARCHAR(255) NOT NULL,
                min VARCHAR(50),
                max VARCHAR(50),
                rate_o VARCHAR(50),
                rate_r VARCHAR(50)
        )""")

        #Crear Tabla De Ordenes (Recibos)
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS Orders(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                id_original INTEGER NOT NULL,
                id_user INTEGER NOT NULL,
                date DATETIME NOT NULL,
                link VARCHAR(4096) NOT NULL,
                charge REAL NOT NULL,
                quantity INTEGER NOT NULL,
                id_service INTEGER NOT NULL
        )""")

        #Finalizar Conexion Con La DB
        self.desconectar_DB()

        #Retorna Que Se Inicializo Bien La DB
        return "DB Orders And Receipt Inicializado Correctamente"

    #Agregar Categoria De Plataforma
    def add_category_plataform(self,name):
        
        #Se Conecta A La DB
        self.conectar_db()

        #Se Realiza El Comando
        self.db.execute(f"""
            SELECT * FROM C_Plataform WHERE name='{name}'
        """)

        #Se Guarda El Resultado
        resp = self.db.fetchall()

        #Se Verifica Que No Exista La Categoria En La DB
        if not resp:
            
            #De No Existir Se Agrega A La DB
            self.db.execute(f" INSERT INTO C_Plataform (name) VALUES ('{name}') ")

            #Se Desconecta De La DB
            self.desconectar_DB()

            #Se Retorna Un Mensaje Notificando
            return self.message_return({"message":"category plataform created"},201)

        #Caso Contrario Se Retorna Que Existe La Categoria Con ID
        else:

            #Se Retorna Un Mensaje Notificando
            return self.message_return({"message":f"category already exists ID : {resp[0][0]}"},400)

    #Agregar Categoria De Servicio
    def add_category_service(self,name,id_c_plataform):
        
        #Se Conecta A La DB
        self.conectar_db()

        #Se Realiza El Comando
        self.db.execute(f"""
            SELECT * FROM C_Service WHERE name='{name}'
        """)

        #Se Guarda El Resultado
        resp = self.db.fetchall()

        #Se Verifica Que No Exista La Categoria En La DB
        if not resp:
            
            #De No Existir Se Agrega A La DB
            self.db.execute(f" INSERT INTO C_Service (name,id_c_plataform) VALUES ('{name}','{id_c_plataform}') ")

            #Se Actualiza La DB
            self.actualizar_DB()

            #Se Desconecta De La DB
            self.desconectar_DB()

            #Se Retorna Un Mensaje Notificando
            return self.message_return({"message":"category service created"},201)

        #Caso Contrario Se Retorna Que Existe La Categoria Con ID
        else:
            
            #Se Retorna Un Mensaje Notificando
            return self.message_return({"message":f"category service already exists ID : {resp[0][0]}"},400)

    #Agregar Servicios
    def add_service(self,id_c_service,name,description,type,min,max,rate_o):
        
        #Se Conecta A La DB
        self.conectar_db()

        #Se Realiza La Consulta En La DB
        self.db.execute(f"""
            SELECT * FROM Service WHERE name='{name}'
        """)

        #Se Guardan Las Respuestas
        resp = self.db.fetchall()

        #Se Verifica Que No Exista El Servicio
        if not resp:

            #De No Existir Se Agrega A La DB
            self.db.execute(f"""
                INSERT INTO Service (id_c_service,name,description,type,min,max,rate_o,rate_r) VALUES ('{id_c_service}','{name}','{description}','{type}','{min}','{max}','{rate_o}','{rate_r})'
            """)

            #Se Actualiza La DB
            self.actualizar_DB()

            #Se Desconecta De La DB
            self.desconectar_DB()

            #Se Retorna Un Mensaje Notificando
            return self.message_return({"message":"service created"},201)

        #Caso Contrario Se Notifica Que Ya Existe
        else:

            #Se Retorna Un Mensaje Notificando
            return self.message_return({"message":f"service already exists ID : {resp[0][0]}"},400)

    #Devolver Datos De Categoria De Plataforma
    def view_category_plataform(self):
        
        #Se Conecta A La DB
        self.conectar_db()

        #Se Consulta En La DB Las Categorias Disponibles
        self.db.execute("""
            SELECT * FROM C_Plataform
        """)

        #Se Almacena Las Respuestas
        resp = self.db.fetchall()

        #Se Desconecta De La DB
        self.desconectar_DB()

        #Variable Provicional
        data = []

        #Se Arma El JSON Iterando Los Objetos
        for id, name in resp:

            #Se Agrega A La Lista
            data.append({"id":id,"name":f"{name}"})

        #Se Retorna El Mensaje Con Su Status
        return self.message_return(data,200)

    #Devolver Datos De Categoria De Servicio
    def view_category_service(self,id_c_plataform):
        
        #Conecar A La DB
        self.conectar_db()

        #Se Realiza La Busqueda
        self.db.execute(f"""
            SELECT * FROM C_Service WHERE id_c_plataform='{id_c_plataform}'
        """)

        #Se Almacena Los Datos Adquiridos
        resp = self.db.fetchall()

        #Se Desconecta De La DB
        self.desconectar_DB()

        #Se Declara Una Variable Recursiva
        data = []

        #Se Arma El JSON Iterando Los Objetos
        for id,id_c_plataforms,name in resp:

            #Se Agrega A La Lista
            data.append({"id":f"{id}","id_c_plataform":f"{id_c_plataforms}","name":f"{name}"})

        #Se Retorna El Mensaje Con Su Status
        return self.message_return(data,200)

    #Devolver Datos De Los Servicios
    def view_services(self,id_c_service):
        
        #Conectar A La DB
        self.conectar_db()

        #Se Realiza La Busqueda En La DB
        self.db.execute(f"""
            SELECT * FROM Service WHERE id_c_service={id_c_service}
        """)

        #Se Almacenan Los Datos
        resp = self.db.fetchall()

        #Desconectamos De La DB
        self.desconectar_DB()

        #Creamos Una Variable Recursiva
        data = []

        #Se Crea El JSON
        for id, id_c_services, name, description, type, min, max, rate_o, rate_r in resp:

            #Se Agrega A La Lista
            data.append({"id":f"{id}","id_c_service":f"{id_c_services}","name":f"{name}","description":f"{description}","type":f"{type}","min":f"{min}","max":f"{max}","rate":f"{rate_r}"})

        #Se Retorna El Mensaje Con Su Status
        return self.message_return(data,200)

#Se Crea La Clase De Ordenes Y Recibos
orders_and_receipt = orders_receipt_db()

#print(orders_and_receipt.inicializar_db())

#print(orders_and_receipt.add_category_plataform("INSTAGRAM"))