from libs.database_c import database_api
from libs.star_lumiere.star_lumire import api_star_lumiere

def add_orders(id_user,link,price,quantity,id_service,type):

    if type == "Default":
        resp = api_star_lumiere.orders_default(id_service,link,quantity)

    elif type == "Otracosa":
        pass
    
    resp_1 = database_api.control_db("INSERT INTO Orders (id_original,id_user,link,price,quantity,id_service) VALUES ('{}','{}','{}','{}','{}','{}')".format(resp['order'],id_user,link,price,quantity,id_service))
    
    return "201"