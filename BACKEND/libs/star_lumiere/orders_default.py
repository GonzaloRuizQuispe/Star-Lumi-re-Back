from libs.database_c import database_api
import requests

def orders_default(id_service,link,quantity,API_URL,API_KEY):

    data = {'key':API_KEY, 'action':'add','service':id_service,'link':link,'quantity':quantity}

    resp_1 = requests.post(API_URL,data=data).json()

    return resp_1