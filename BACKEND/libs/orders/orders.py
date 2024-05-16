from libs.orders.add_category_plataform import add_category_plataform
from libs.orders.add_category_service import add_category_service
from libs.orders.add_service import add_service

from libs.orders.view_category_plataform import view_category_plataform
from libs.orders.view_category_service import view_category_service
from libs.orders.view_services import view_services

from libs.orders.add_orders import add_orders

class orders_receipt_db():
    
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

    def add_orders(self,id_user,link,price,quantity,id_service,type):
        return add_orders(id_user,link,price,quantity,id_service,type)

    def change_description(self):
        pass

    def change_c_service(self):
        pass

    def change_c_plataform(self):
        pass

#Se Crea La Clase De Ordenes Y Recibos
orders_api = orders_receipt_db()

#print(orders_and_receipt.inicializar_db())

#print(orders_and_receipt.add_category_plataform("TIKTOK"))

#print(orders_and_receipt.add_category_service('New 🔥 | Instagram Services',"1"))