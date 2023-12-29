import sqlite3

#API_KEY = "e7b761  fad2ea99e47e529cad1a06671f" #Infinity
#API_URL = "https://infinityupgraders.com/api/v2" #Infinity

#API_KEY = "393791242c29a4efc1b2a98b20afd364" #Original?
#API_URL = "https://worldofsmm.com/api/v2" #Original?

class orders_receipt_db():

    #Variables Recursiva
    conexion = None
    db = None

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

    #Inicializar DB
    def inicializar_db(self):

        #Conectar A La DB
        self.conectar_db()

        #Crear Tabla Category Plataform Si Es Que No Existe
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS C_Plataform(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(255) NOT NULL
        )""")

        #Crear Tabla Category Services Si Es Que No Existe
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS C_Service(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_c_plataform INTEGER NOT NULL,
                name VARCHAR(255) NOT NULL,
                FOREIGN KEY (id_c_plataform) REFERENCES C_Plataform(id)
        )""")

        #Crear Tabla Servicios Si Es Que No Existe
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS Service(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_c_service INTEGER NOT NULL,
                name VARCHAR(255) NOT NULL,
                description VARCHAR(255),
                type VARCHAR(255) NOT NULL,
                min VARCHAR(50),
                max VARCHAR(50),
                rate_o VARCHAR(50),
                rate_r VARCHAR(50),
                FOREIGN KEY (id_c_service) REFERENCES C_Service(id)
        )""")

        #Crear Tabla De Ordenes (Recibos)
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS Orders(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_original INTEGER NOT NULL,
                id_user INTEGER NOT NULL,
                date DATETIME NOT NULL,
                link VARCHAR(999999) NOT NULL,
                charge REAL NOT NULL,
                quantity INTEGER NOT NULL,
                id_service INTEGER NOT NULL,
                FOREIGN KEY (id_service) REFERENCES Service(id),
                FOREIGN KEY (id_user) REFERENCES Data(id)
        )""")

        #Actualizar La DB
        self.actualizar_DB()

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

            #Se Actualiza La DB
            self.actualizar_DB()

            #Se Desconecta De La DB
            self.desconectar_DB()

            #Retorna Mensaje Valido
            return {'Resultado':'Valido'}

        #Caso Contrario Se Retorna Que Existe La Categoria Con ID
        else:
            return {'Resultado':{'Category Exists ID':f'{resp[0][0]}'}}

    #Agregar Categoria De Servicio
    def add_category_service(self):
        pass
  
#Se Crea La Clase De Ordenes Y Recibos
orders_and_receipt = orders_receipt_db()

print(orders_and_receipt.inicializar_db())

#print(orders_and_receipt.add_category_plataform('TIKTOK'))