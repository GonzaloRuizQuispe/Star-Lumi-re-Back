from libs.services.add_category_plataform import add_category_plataform

from libs.services.view_category_plataform import view_category_plataform
from libs.services.view_category_service import view_category_service
from libs.services.view_services import view_services

class services():

    def add_category_plataform(self,name):
        return add_category_plataform(name)

    def view_category_plataform(self):
        return view_category_plataform()

    def view_category_service(self,id_c_plataform):
        return view_category_service(id_c_plataform)

    def view_services(self,name):
        return view_services(name)


#Se Crea La Clase De Ordenes Y Recibos
services_api = services()

#print(orders_and_receipt.inicializar_db())

#print(orders_and_receipt.add_category_plataform("TIKTOK"))

#print(orders_and_receipt.add_category_service('New 🔥 | Instagram Services',"1"))