from libs.database_c import database_api
from libs.star_lumiere.star_lumire import api_star_lumiere
from libs.users.usuarios import usuarios_api

def add_orders(id_user,link,price,quantity,id_service,type,balance):

    if type == "Default":
        resp = api_star_lumiere.orders_default(id_service,link,quantity)

    elif type == "Otracosa":
        pass
    
    resp_1 = database_api.control_db("INSERT INTO Orders (id_original,id_user,link,price,quantity,id_service) VALUES ('{}','{}','{}','{}','{}','{}')".format(resp['order'],id_user,link,price,quantity,id_service))
    resp_2 = usuarios_api.cambiar_balance((float(balance)-float(price)),id_user)

    return "201"