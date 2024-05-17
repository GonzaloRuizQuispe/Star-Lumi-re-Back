from libs.services.add_category_plataform import add_category_plataform
from libs.services.add_category_service import add_category_service
from libs.services.add_service import add_service

from libs.services.view_category_plataform import view_category_plataform
from libs.services.view_category_service import view_category_service
from libs.services.view_services import view_services

from libs.services.change_description import change_description
from libs.services.change_c_service import change_c_service
from libs.services.change_c_plataform import change_c_plataform

class services():
    
    def add_category_plataform(self,name):
        return add_category_plataform(name)

    def add_category_service(self,name,id_c_plataform):
        return add_category_service(name,id_c_plataform)

    def add_service(self,id_original,id_c_service,description):
        return add_service(id_original,id_c_service,description)

    def view_category_plataform(self):
        return view_category_plataform()

    def view_category_service(self,id_c_plataform):
        return view_category_service(id_c_plataform)

    def view_services(self,id_c_service):
        return view_services(id_c_service)

    def change_description(self,id_service,description):
        return change_description(id_service,description)

    def change_c_service(self,id_service,id_c_service): #Actua Sobre Un Servicio
        return change_c_service(id_service,id_c_service)

    def change_c_plataform(self,id_c_service,id_c_plataform): #Actua Sobre Una C_Service
        return change_c_plataform(id_c_service,id_c_plataform)

#Se Crea La Clase De Ordenes Y Recibos
services_api = services()

#print(orders_and_receipt.inicializar_db())

#print(orders_and_receipt.add_category_plataform("TIKTOK"))

#print(orders_and_receipt.add_category_service('New 🔥 | Instagram Services',"1"))