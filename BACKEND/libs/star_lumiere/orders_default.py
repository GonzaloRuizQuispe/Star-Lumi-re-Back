from libs.database_c import database_api
import requests

def orders_default(id,link,quantity,API_URL,API_KEY):
    resp = database_api.control_db("SELECT * FROM Service WHERE id='{}'".format(id))

    data = {'key':API_KEY, 'action':'add','service':resp[0][1],'link':link,'quantity':quantity}

    resp_1 = requests.post(API_URL,data=data).json()

    return resp_1