from libs.database_c import database_api
from libs.star_lumiere.star_lumire import api_star_lumiere
from libs.users.usuarios import usuarios_api

def add_orders(id_user,link,quantity,id_service):

    resp_star = api_star_lumiere.view_services()

    for x in resp_star:
        if int(x['service']) == int(id_service):
            service = x
        else:
            pass

    if service['type'] == "Default":
        resp = api_star_lumiere.orders_default(id_service,link,quantity)
        pass

    elif service['type'] == "Otracosa":
        pass
    
    resp_db = database_api.control_db("SELECT * FROM Usuarios WHERE id='{}'".format(id_user))

    price = ((float(service['rate'])/100)*float(quantity))
    balance_user = float(resp_db[0][7])
    new_balance = balance_user - price

    resp_1 = database_api.control_db("INSERT INTO Orders (id_original,id_user,link,price,quantity,id_service) VALUES ('{}','{}','{}','{}','{}','{}')".format(resp['order'],id_user,link,price,quantity,id_service))
    
    resp_2 = usuarios_api.cambiar_balance(new_balance,id_user)

    json = {"id_order":resp_1,"new_balance":new_balance}

    return database_api.message_return(json,201)