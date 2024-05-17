from libs.orders.add_orders import add_orders

class orders():
    
    def add_orders(self,id_user,link,price,quantity,id_service,type,balance):
        return add_orders(id_user,link,price,quantity,id_service,type,balance)
        
api_orders = orders()