from libs.database_c import database_api
import requests

def view_services_ids(tuple_ids,API_KEY,API_URL):
    #Se Llena La Accion A Realizar
        data = {'key':API_KEY, 'action':'services'}

        #Se Hace La Consulta
        resp = requests.post(API_URL,data=data).json()

        data = []

        for x in resp:
            if x['service'] in str(tuple_ids):
                data.append({"id":x['service'],"name":x["name"], "type":x["type"], "rate":x["rate"], "min":x["min"], "max":x["max"]})

        return data