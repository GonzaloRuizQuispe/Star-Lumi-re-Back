from libs.orders.add_category_plataform import add_category_plataform
from libs.orders.add_category_service import add_category_service
from libs.orders.add_service import add_service

class orders_receipt_db():
    
    def add_category_plataform(self,name):
        return add_category_plataform(name)

    def add_category_service(self,name,id_c_plataform):
        return add_category_service(name,id_c_plataform)

    def add_service(self,id_original,id_c_service,description):
        return add_service(id_original,id_c_service,description)








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
        for id, id_original, id_c_service, name, description, type, min, max, rate_o, rate_r in resp:
            
            #Se Agrega A La Lista
            data.append({"id":f"{id}","id_original":f"{id_original}","id_c_service":f"{id_c_service}","name":f"{name}","description":f"{description}","type":f"{type}","min":f"{min}","max":f"{max}","rate":f"{rate_r}"})

        #Se Retorna El Mensaje Con Su Status
        return self.message_return(data,200)

#Se Crea La Clase De Ordenes Y Recibos
orders_and_receipt = orders_receipt_db()

#print(orders_and_receipt.inicializar_db())

#print(orders_and_receipt.add_category_plataform("TIKTOK"))

#print(orders_and_receipt.add_category_service('New 🔥 | Instagram Services',"1"))