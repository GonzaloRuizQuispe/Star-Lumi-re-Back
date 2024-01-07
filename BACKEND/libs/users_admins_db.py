import sqlite3
import pyotp
from flask import make_response

class users_admins_db():

    #Variables Recursiva
    conexion = None
    db = None
    codigo = "B5YY3Q3HOXTK6XCW3SYJIEEVKFM2J3P3"

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
        self.conexion = sqlite3.connect('BACKEND/database/database.db')

        #Crear Cursos Para Comandos
        self.db = self.conexion.cursor()

    #Desconecarse De La DB
    def desconectar_DB(self):

        #Cerrar DB
        self.conexion.close()

    #Actualizar DB
    def actualizar_DB(self):

        #Actulizar DB
        self.conexion.commit()

    #Inicializar La DB Si Es Que No Existe
    def inicializar_db(self):

        #Conectarse DB
        self.conectar_db()

        #Crear Tabla Admins
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS Administrador(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(999999) NOT NULL,
                password VARCHAR(999999) NOT NULL,
                email VARCHAR(999999) NOT NULL,
                token_header VARCHAR(64) NOT NULL,
                token_acceso VARCHAR(32) NOT NULL,
                rol VARCHAR (50) NOT NULL DEFAULT 'Administrador',
                balance REAL NOT NULL
        )""")

        #Crear Tabla Usuarios
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS Usuario(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(999999) NOT NULL,
                password VARCHAR(999999) NOT NULL,
                email VARCHAR(999999) NOT NULL,
                token_header VARCHAR(64) NOT NULL,
                token_acceso VARCHAR(32) NOT NULL,
                rol VARCHAR (50) NOT NULL DEFAULT 'Usuario',
                balance REAL NOT NULL
        )""")

        #Crear Tabla Datos
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS Data(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR (999999) NOT NULL,
                email VARCHAR (999999) NOT NULL,
                token_header VARCHAR (64) NOT NULL,
                token_acceso VARCHAR (32) NOT NULL,
                rol VARCHAR (50) NOT NULL,
                balance REAL NOT NULL
            )
        """)

        #Crear Trigger Para Llenar La Tabla Data Con Usuarios
        self.db.execute('''
            CREATE TRIGGER IF NOT EXISTS agregar_token_usuario
            AFTER INSERT ON Usuario 
            BEGIN
                INSERT INTO data (username, email, token_header, token_acceso, rol, balance)
                VALUES (NEW.username, NEW.email, NEW.token_header, NEW.token_acceso, NEW.rol, NEW.balance);
            END;
        ''')

        #Crear Trigger Para Actualizar Cambios De La Tabla Data Con Usuarios
        self.db.execute('''
            CREATE TRIGGER IF NOT EXISTS actualizar_data_usuarios
            AFTER UPDATE ON Usuario 
            BEGIN
                UPDATE data
                SET 
                    username = COALESCE(NEW.username, data.username),
                    email = COALESCE(NEW.email, data.email),
                    balance = COALESCE(NEW.balance, data.balance)
                WHERE data.token_header = NEW.token_header;
            END;
        ''')

        #Crear Trigger Para Llenar La Tabla Data Con Administradores
        self.db.execute('''
            CREATE TRIGGER IF NOT EXISTS agregar_token_administrador
            AFTER INSERT ON Administrador 
            BEGIN
                INSERT INTO data (username, email, token_header, token_acceso, rol, balance)
                VALUES (NEW.username, NEW.email, NEW.token_header, NEW.token_acceso, NEW.rol, NEW.balance);
            END;
        ''')

        #Crear Trigger Para Actualizar Cambios De La Tabla Data Con Administradores
        self.db.execute('''
            CREATE TRIGGER IF NOT EXISTS actualizar_data_administradores
            AFTER UPDATE ON Administrador 
            BEGIN
                UPDATE data
                SET 
                    username = COALESCE(NEW.username, data.username),
                    email = COALESCE(NEW.email, data.email),
                    balance = COALESCE(NEW.balance, data.balance)
                WHERE data.token_header = NEW.token_header;
            END;
        ''')

        #Actualizar DB
        self.actualizar_DB()

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

                #Commit En La DB
                self.actualizar_DB()

                #Finalizar Conexion
                self.desconectar_DB()

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

                #Commit En La DB
                self.actualizar_DB()

                #Finalizar Conexion
                self.desconectar_DB()

                #Se Retorna Un Mensaje Notificando
                return self.message_return({"message":"user created"},201)

        #Caso Contrario Se Revisa El Error Y Se Envia Para Ser Cambiado
        else:
                
            #Desconectar De La DB
            self.desconectar_DB()
            
            #Si El Usuario Y El Correo Ya Existen
            if username == resp[0][1] and email == resp[0][2]:

                #Se Retorna Un Mensaje Notificando
                return self.message_return({"message" : "username y email en uso"},400)

            #Si El Usuario Existe Pero El Correo No
            elif username == resp[0][1] and not (email == resp[0][2]):

                #Se Retorna Un Mensaje Notificando
                return self.message_return({"message" : "username en uso"},400)

            #Si El Correo Existe Pero El Usuario No
            elif not (username == resp[0][1]) and email == resp[0][2]:

                #Se Retorna Un Mensaje Notificando
                return self.message_return({"message" : "email en uso"},400)

    #Modificar Balance
    def balance_update(self,id_usuario,balance_update,rol):

        #Conectar DB
        self.conectar_db()

        #Extraer Balance Original Para Sumarle El Nuevo
        self.db.execute(f"""
            SELECT * FROM {rol} WHERE id='{id_usuario}'
        """)

        #Se Guarda La Respuesta De Busqueda
        resp = self.db.fetchall()

        #Se Modifica El Balance Del Usuario Mediante Su ID (Visible En WEB)
        self.db.execute(f"""
            UPDATE {rol} SET balance='{float(resp[0][7])+float(balance_update)}' WHERE id='{int(id_usuario)}'
        """)

        #Actualizar Cambios
        self.actualizar_DB()
        
        #Desconectar De La DB
        self.desconectar_DB()
        
    #Devolver Datos Por Email/Contraseña
    def login_email_pass(self,email,password):
        
        #Conectar DB
        self.conectar_db()

        #Se Realiza La Busqueda
        self.db.execute(f"""
            SELECT * FROM Data WHERE email='{email}'
        """)

        #Se Almacena La Respuesta
        resp = self.db.fetchall()

        #Si Existe El Email Segun Su Rol Se Verifica En Su Tabla
        if resp:

            #Se Realiza La Busqueda Por Rol Del Email Y Contraseña
            self.db.execute(f"""
                SELECT * FROM {resp[0][5]} WHERE email='{email}' and password='{password}'
            """)

            #Se Almance La Respuesta
            resp_2 = self.db.fetchall()

            #Si Existe Coincidencia Se Retornan Todos Los Datos
            if resp_2:

                #Se Retorna El Mensaje
                return self.message_return({"id":resp[0][0],"username":resp[0][1],"email":resp[0][2],"token_header":resp[0][3],"rol":resp[0][5],"balance":resp[0][6]},200)
            
            #Caso Contrario Se Retorna Contraseña Invalida
            else:
                
                #Se Retorna El Mensaje
                return self.message_return({"message":"invalid password"},404)

        #Caso Contrario Se Retorna Invalido
        else:

            #Se Retorna El Mensaje
            return self.message_return({"message":"invalid email"},404)

    #Devolver Datos Por Token Header
    def login_token_header(self,token_header):

        #Conectar DB
        self.conectar_db()

        #Se Realiza La Busqueda
        self.db.execute(f"""
            SELECT * FROM Data WHERE token_header = '{token_header}'
        """)

        #Se Almacenan Los Resultados De La Busqueda
        resp = self.db.fetchall()

        #Desconectar De La DB
        self.desconectar_DB()
        
        #De Existir Se Retornan Su Datos
        if resp:

            #Se Retorna El Mensaje
            return self.message_return({"id":resp[0][0],"username":resp[0][1],"email":resp[0][2],"token_header":resp[0][3],"rol":resp[0][5],"balance":resp[0][6]},200)

        #Caso Contrario Se Retorna Invalido
        else:
            
            #Se Retorna El Mensaje
            return self.message_return({"message":"invalid token"},401)

#Se Crea La Clase DB
users_and_admins = users_admins_db()

#Iniciar
print(users_and_admins.inicializar_db())

#print(users_and_admins.agregar_user('Test1','Keka4542','Test1@gmail.com','Usuario'))