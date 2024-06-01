from libs.orders.add_orders import add_orders

class orders():
    
    def add_orders(self,id_user,link,quantity,id_service,type):
        return add_orders(id_user,link,quantity,id_service,type)
        
api_orders = orders()