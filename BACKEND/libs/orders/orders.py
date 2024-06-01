from libs.orders.add_orders import add_orders

class orders():
    
    def add_orders(self,id_user,link,quantity,id_service):
        return add_orders(id_user,link,quantity,id_service)
        
api_orders = orders()