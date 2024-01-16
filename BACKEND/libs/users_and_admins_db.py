import pyotp
from flask import make_response
from dotenv import load_dotenv
import os
import pymysql

class users_and_admins():

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

    #Desconecarse De La DB
    def desconectar_DB(self):

        #Cerrar Cursor Y DB
        self.db.close()
        self.conexion.close()

    #Inicializar La DB Si Es Que No Existe
    def inicializar_db(self):

        #Conectarse DB
        self.conectar_db()

        #Crear Tabla Admins
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS Administrador(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                username VARCHAR(1024) NOT NULL,
                password VARCHAR(1024) NOT NULL,
                email VARCHAR(1024) NOT NULL,
                token_header VARCHAR(64) NOT NULL,
                token_acceso VARCHAR(32) NOT NULL,
                rol VARCHAR (50) NOT NULL DEFAULT 'Administrador',
                balance REAL NOT NULL
        )""")

        #Crear Tabla Usuarios
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS Usuario(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                username VARCHAR(1024) NOT NULL,
                password VARCHAR(1024) NOT NULL,
                email VARCHAR(1024) NOT NULL,
                token_header VARCHAR(64) NOT NULL,
                token_acceso VARCHAR(32) NOT NULL,
                rol VARCHAR (50) NOT NULL DEFAULT 'Usuario',
                balance REAL NOT NULL
        )""")

        #Crear Tabla Token_Header By Rol
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS Data(
                username VARCHAR(1024) NOT NULL,
                password VARCHAR(1024) NOT NULL,
                email VARCHAR(1024) NOT NULL,
                token_header VARCHAR(64) NOT NULL,
                token_acceso VARCHAR(32) NOT NULL,
                rol VARCHAR (50) NOT NULL 
            )
        """)

        #Desconectar DB
        self.desconectar_DB

        #Retorna Que Se Inicializo Bien La DB
        return "DB Users And Admins Inicializado Correctamente"

    #Certificar Codigo OTP Para Usar Funciones
    def code_rol_validation(self, current_password):

        #Si La Contraseña No Se Envia Retorna Falso
        if current_password == None:
            return False

        #Si La Contraseña Es Una Cadena Vacia Retorna Falso
        if not current_password:
            return False

        #Si La Contraseña Es De Caracter Valido Se Genera El TOTP
        totp = pyotp.TOTP(self.codigo)

        #Si La Contraseña Es Correcta En Tiempo Real Se Retorna True
        if totp.verify(current_password):
            return True

        #Si No Coincide Se Retorna False
        return False

    #Generar Token Header Para Los Usuarios/Administradores
    def gen_token_header(self):

        #Se Genera El Token
        token = pyotp.random_base32(length=64)

        #No Requiere De Conectarse Ya Que Se Usa Dentro De Otra Funcion
        #Se Consulta En La DB La Tabla De "Data" Si Existe Algun Token Similar
        self.db.execute(f"""
            SELECT * FROM Data WHERE token_header = '{token}'
        """)

        #Se Guarda La Respuesta
        resp = self.db.fetchall()

        #De No Hallar Similitud Se Retorna La Cadena
        if not resp:
            return token
        #Caso Contrario Se Vuelve A Ejecutar La Funcion
        else:
            return self.gen_token_header()
        
    #Generar Token Acceso Para Los Usuarios/Administradores
    def gen_token_acceso(self):

        #Se Genera El Token
        token = pyotp.random_base32(length=32)

        #No Requiere De Conectarse Ya Que Se Usa Dentro De Otra Funcion
        #Se Consulta En La DB La Tabla De "Data" Si Existe Algun Token Similar
        self.db.execute(f"""
            SELECT * FROM Data WHERE token_acceso = '{token}'
        """)

        #Se Guarda La Respuesta
        resp = self.db.fetchall()

        #De No Hallar Similitud Se Retorna La Cadena
        if not resp:
            return token
        #Caso Contrario Se Vuelve A Ejecutar La Funcion
        else:
            return self.gen_token_acceso()

    #Trigger Insert Data
    def trigger_data(self,username,password,email,token_header,token_acceso,rol):

        #Conectar DB
        self.conectar_db()

        #Agregar Datos
        self.db.execute(f"""
            INSERT INTO Data (username,password,email,token_header,token_acceso,rol) VALUES ('{username}','{password}','{email}','{token_header}','{token_acceso}','{rol}')
        """)

    #Agregar Usuario
    def agregar_user(self, username, password, email, rol, codigo=None):
        
        #Conectarse A La DB
        self.conectar_db()

        #Buscar Similitud En Los Datos
        self.db.execute(f"""
            SELECT * FROM Data WHERE username='{username}' or email='{email}'
        """)

        #Se Guardan Los Valores
        resp = self.db.fetchall()
    
        #De No Hallar Similitud Se Agrega El Usuario
        if not resp:

            #Generar Token Header
            token_header = self.gen_token_header()

            #Generar Token Acceso
            token_acceso = self.gen_token_acceso()

            #Si El Rol Es Un Administrador Y El Codigo Es Correcto Se Añade Via "ADMIN"
            if ((rol == 'Administrador') and (self.code_rol_validation(codigo))):
                
                #Agregar Valores
                self.db.execute(f"""
                    INSERT INTO {rol} (username,password,email,token_header,token_acceso,balance) VALUES ('{username}','{password}','{email}','{token_header}','{token_acceso}','0')
                """)

                #Finalizar Conexion
                self.desconectar_DB()

                #Trigger Data
                self.trigger_data(username,password,email,token_header,token_acceso,rol)

                #Se Retorna Un Mensaje Notificando
                return self.message_return({"message":"user created"},201)

            #Si El Rol Es Un Administrador Y El Codigo Es Incorrecto Se Notifica El Error
            elif ((rol == 'Administrador') and not(self.code_rol_validation(codigo))):
                
                #Se Retorna Un Mensaje Notificando
                return self.message_return({"message":"code invalid"},400)


            #Si El Rol Es Un Usuario Y No Tiene Codigo Se Añade Via "USER"
            elif rol == 'Usuario':

                #Agregar Valores
                self.db.execute(f"""
                    INSERT INTO {rol} (username,password,email,token_header,token_acceso,balance) VALUES ('{username}','{password}','{email}','{token_header}','{token_acceso}','0')
                """)

                #Finalizar Conexion
                self.desconectar_DB()

                #Trigger Data
                self.trigger_data(username,password,email,token_header,token_acceso,rol)

                #Se Retorna Un Mensaje Notificando
                return self.message_return({"message":"user created"},201)

        #Caso Contrario Se Revisa El Error Y Se Envia Para Ser Cambiado
        else:
            
            #Desconectar De La DB
            self.desconectar_DB()
            
            #Si El Usuario Y El Correo Ya Existen
            if username == resp[0][0] and email == resp[0][2]:

                #Se Retorna Un Mensaje Notificando
                return self.message_return({"message" : "username y email en uso"},400)

            #Si El Usuario Existe Pero El Correo No
            elif username == resp[0][0] and not (email == resp[0][2]):

                #Se Retorna Un Mensaje Notificando
                return self.message_return({"message" : "username en uso"},400)

            #Si El Correo Existe Pero El Usuario No
            elif not (username == resp[0][0]) and email == resp[0][2]:

                #Se Retorna Un Mensaje Notificando
                return self.message_return({"message" : "email en uso"},400)

    #Identificar Rol Con Token Header
    def identify_rol_token_header(self,token_header):
        
        #Conectar DB
        self.conectar_db()

        #Realizar Consulta
        self.db.execute(f"""
            SELECT * FROM Data WHERE token_header='{token_header}'
        """)

        #Guardar Respuesta
        resp = self.db.fetchall()

        #Desconectar DB
        self.desconectar_DB()

        #Si El Token No Existe Se Retorna Falso
        if not resp:
            
            return False

        #Caso Contrario Se Retorna El Rol
        else:
            #Retornar Mensaje Con El Rol
            return resp[0][5]

    #Identificar Rol Con Email, Password
    def identify_rol_email_password(self,email,password):
        
        #Conectar DB
        self.conectar_db()

        #Realizar Consulta
        self.db.execute(f"""
            SELECT * FROM Data WHERE email='{email}' and password='{password}'
        """)

        #Guardar Respuesta
        resp = self.db.fetchall()

        #Desconectar DB
        self.desconectar_DB()

        #Si Esta Vacio Se Retorna Falso
        if not resp:

            return False

        #Caso Contrario Se Retorna El Rol
        else:

            #Retornar Mensaje Con El Rol
            return resp[0][5]

    #Modificar Balance
    def balance_update(self,token_header,balance_update):

        #Identificar Rol
        rol = self.identify_rol_token_header(token_header)

        #Conectar DB
        self.conectar_db()

        #Extraer Balance Original Para Sumarle El Nuevo
        self.db.execute(f"""
            SELECT * FROM {rol} WHERE token_header='{token_header}'
        """)

        #Se Guarda La Respuesta De Busqueda
        resp = self.db.fetchall()

        #Se Modifica El Balance Del Usuario Mediante Su ID (Visible En WEB)
        self.db.execute(f"""
            UPDATE {rol} SET balance='{float(resp[0][7])+float(balance_update)}' WHERE id='{int(id_usuario)}'
        """)

        #Desconectar De La DB
        self.desconectar_DB()

        #Retorna Mensaje Junto Al Status
        return self.message_return({"message":"balance update"},201)

    #Devolver Datos Por Email/Contraseña
    def login_email_pass(self,email,password):
        
        #Identificar Rol
        rol = self.identify_rol_email_password(email,password)

        if rol:

            #Conectar DB
            self.conectar_db()

            #Se Realiza La Busqueda
            self.db.execute(f"""
                SELECT * FROM {rol} WHERE email='{email}'
            """)

            #Se Almacena La Respuesta
            resp = self.db.fetchall()

            #Si Existe El Email Segun Su Rol Se Verifica En Su Tabla
            if resp:

                #Se Realiza La Busqueda Por Rol Del Email Y Contraseña
                self.db.execute(f"""
                    SELECT * FROM {rol} WHERE email='{email}' and password='{password}'
                """)

                #Se Almance La Respuesta
                resp_2 = self.db.fetchall()

                #Si Existe Coincidencia Se Retornan Todos Los Datos
                if resp_2:

                    #Se Retorna El Mensaje
                    return self.message_return({"id":resp[0][0],"username":resp[0][1],"email":resp[0][3],"token_header":resp[0][4],"rol":resp[0][6],"balance":resp[0][7]},200)
                
                #Caso Contrario Se Retorna Contraseña Invalida
                else:
                    
                    #Se Retorna El Mensaje
                    return self.message_return({"message":"invalid password"},404)

            #Caso Contrario Se Retorna Invalido
            else:

                #Se Retorna El Mensaje
                return self.message_return({"message":"invalid email"},404)
        
        #Si Esta Vacio Rol Indica Que La Cuenta No Existe
        else:

            #Se Retorna El Mensaje
            return self.message_return({"message":"invalid email"},404)

    #Devolver Datos Por Token Header
    def login_token_header(self,token_header):

        #Identificar Rol Con Token Header
        rol = self.identify_rol_token_header(token_header)

        #Si El Rol Existe Se Retornan Sus Datos
        if rol:

            #Conectar DB
            self.conectar_db()

            #Se Realiza La Busqueda
            self.db.execute(f"""
                SELECT * FROM {rol} WHERE token_header = '{token_header}'
            """)

            #Se Almacenan Los Resultados De La Busqueda
            resp = self.db.fetchall()

            #Desconectar De La DB
            self.desconectar_DB()
            
            #De Existir Se Retornan Su Datos
            if resp:

                #Se Retorna El Mensaje
                return self.message_return({"id":resp[0][0],"username":resp[0][1],"email":resp[0][3],"token_header":resp[0][4],"rol":resp[0][6],"balance":resp[0][7]},200)

            #Caso Contrario Se Retorna Invalido
            else:
                
                #Se Retorna El Mensaje
                return self.message_return({"message":"invalid token"},401)
        
        #Caso Contrario No Existe Cuenta Con Ese Token
        else:

            #Se Retorna El Mensaje
            return self.message_return({"message":"invalid token"},401)

#Se Crea La Clase DB
users_admins_db = users_and_admins()

#Iniciar
print(users_admins_db.inicializar_db())

#print(users_admins_db.balance_update("RYZVKNNUNNDXBNCUR6S3YTBHB2UKPRPDIZN2SZPPVXQUM5QAHS54DOAKICUYL4GC",5))

#print(users_admins_db.login_email_pass("Test1@gmail.com","Keka4542"))

#print(users_admins_db.identify_rol_token_header("RYZVKNNUNNDXBNCUR6S3YTBHB2UKPRPDIZN2SZPPVXQUM5QAHS54DOAKICUYL4GC"))

#print(users_admins_db.login_token_header("GW3T2GBNAVPMT2AX26TYFJZPQCQTT4JTEPODDKK5X77INMWU576WA5ORYNZN3CMJ"))