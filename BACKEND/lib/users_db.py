import sqlite3

class users_db():

    #Variables Recursiva
    conexion = None
    db = None

    #Conectarse A La DB
    def conectar_db(self):

        #Crear Conexion
        self.conexion = sqlite3.connect('BACKEND/database/users.db')

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

    def inicializar_db(self):

        #Conectarse DB
        self.conectar_db()

        #Crear/Usar Tabla
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS usuarios(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(999999) NOT NULL,
                password VARCHAR(999999) NOT NULL,
                email VARCHAR(999999) NOT NULL,
                token_header VARCHAR(64) NOT NULL,
                token_acceso VARCHAR(32) NOT NULL,
                balance REAL NOT NULL
        )""")

        #Actualizar DB
        self.actualizar_DB()

        #Desconectar DB
        self.desconectar_DB

    #Agregar Usuario
    def agregar_user(self,username,password,email,token_header,token_acceso):
        
        #Conectarse A La DB
        self.conectar_db()

        #Buscar Similitud En Los Datos
        self.db.execute(f"""
            SELECT * FROM usuarios WHERE username='{username}' or email='{email}'
        """)

        #Se Guardan Los Valores
        resp = self.db.fetchall()

        #De No Hallar Similitud Se Agrega El Usuario
        if not resp:
            #Agregar Valores
            self.db.execute(f"""
                INSERT INTO usuarios (username,password,email,token_header,token_acceso,balance) VALUES ('{username}','{password}','{email}','{token_header}','{token_acceso}','0')
            """)

            #Commit En La DB
            self.actualizar_DB()

            #Finalizar Conexion
            self.desconectar_DB()

        #Caso Contrario Se Revisa El Error Y Se Envia Para Ser Cambiado
        else:
                
            #Desconectar De La DB
            self.desconectar_DB()
            
            #Si El Usuario Y El Correo Ya Existen
            if username == resp[0][1] and email == resp[0][3]:
                return {'Resultado' : {'Error Repeat':{'Username','Email'}}}

            #Si El Usuario Existe Pero El Correo No
            elif username == resp[0][1] and not (email == resp[0][3]):
                return {'Resultado' : {{'Error Repeat':'Username'}}}

            #Si El Correo Existe Pero El Usuario No
            elif not (username == resp[0][1]) and email == resp[0][3]:
                return {'Resultado' : {{'Error Repeat':'Email'}}}

    #Verificar Tokens
    def find_token_header(self,token_header):

        #Conectar DB
        self.conectar_db()

        #Se Realiza La Busqueda
        self.db.execute(f"""
            SELECT * FROM usuarios WHERE token_header = '{token_header}'
        """)

        #Se Almacenan Los Resultados De La Busqueda
        resp = self.db.fetchall()

        #Desconectar De La DB
        self.desconectar_DB()
        
        #De No Existir Se Retorna Valido
        if not resp:
            return {'Resultado':'Valido'}
        
        #Caso Contrario Se Retorna Invalido
        else:
            return {'Resultado':'Invalido'}

    #Verificar Tokens
    def find_token_acceso(self,token_acceso):

        #Conectar DB
        self.conectar_db()

        #Se Realiza La Busqueda
        self.db.execute(f"""
            SELECT * FROM usuarios WHERE token_acceso = '{token_acceso}'
        """)

        #Se Almacenan Los Resultados De La Busqueda
        resp = self.db.fetchall()

        #Desconectar De La DB
        self.desconectar_DB()

        #De No Existir Se Retorna Valido
        if not resp:
            return {'Resultado':'Valido'}
        
        #Caso Contrario Se Retorna Invalido
        else:
            return {'Resultado':'Invalido'}

    #Modificar Balance
    def balance_update(self,id_usuario,balance_update):

        #Conectar DB
        self.conectar_db()

        #Extraer Balance Original Para Sumarle El Nuevo
        self.db.execute(f"""
            SELECT * FROM usuarios WHERE id='{id_usuario}'
        """)

        #Se Guarda La Respuesta De Busqueda
        resp = self.db.fetchall()

        #Se Modifica El Balance Del Usuario Mediante Su ID (Visible En WEB)
        self.db.execute(f"""
            UPDATE usuarios SET balance='{float(resp[0][6])+float(balance_update)}' WHERE id='{int(id_usuario)}'
        """)

        #Actualizar Cambios
        self.actualizar_DB()
        
        #Desconectar De La DB
        self.desconectar_DB()
        

#Se Crea La Clase DB
database = users_db()

#Iniciar
database.inicializar_db()