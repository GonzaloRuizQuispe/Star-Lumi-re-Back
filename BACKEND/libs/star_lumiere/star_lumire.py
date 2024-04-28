import requests
from dotenv import load_dotenv
import os

class star_lumiere():

    #Cargar Datos De .env
    load_dotenv()

    #Key Para Vincular A La Cuenta Original
    API_KEY = os.getenv("API_KEY") #SMM ENGINER

    #Link Que Conecta Con La API
    API_URL = os.getenv("API_URL") #SMM ENGINER

    #En Cabezado Para Evitar Errores
    headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)'}

    def view_service(self,tuple_ids):

        #Se Llena La Accion A Realizar
        data = {'key':self.API_KEY, 'action':'services'}

        #Se Hace La Consulta
        resp = requests.post(self.API_URL,data=data).json()

        data = []

        for x in resp:
            if x['service'] in tuple_ids:
                data.append({"name":x["name"], "type":x["type"], "rate":x["rate"], "min":x["min"], "max":x["max"]})

        return data

    def user_balance(self):
        data = {'key':self.API_KEY, 'action':'balance'}
        resp = requests.post(self.API_URL,data=data).json()
        return resp

api_star_lumiere = star_lumiere()

#print(api_star_lumiere.view_service(("15077","15493")))