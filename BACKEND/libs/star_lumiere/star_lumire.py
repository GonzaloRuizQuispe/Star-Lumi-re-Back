import requests
from dotenv import load_dotenv
import os

from star_lumiere.view_categories import view_categorys
from star_lumiere.view_services import view_services

class star_lumiere():

    #Cargar Datos De .env
    load_dotenv()

    #Key Para Vincular A La Cuenta Original
    API_KEY = os.getenv("API_KEY") #SMM ENGINER

    #Link Que Conecta Con La API
    API_URL = os.getenv("API_URL") #SMM ENGINER

    #En Cabezado Para Evitar Errores
    headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)'}

    def view_service_ids(self,tuple_ids):

        #Se Llena La Accion A Realizar
        data = {'key':self.API_KEY, 'action':'services'}

        #Se Hace La Consulta
        resp = requests.post(self.API_URL,data=data).json()

        data = []

        for x in resp:
            if x['service'] in str(tuple_ids):
                data.append({"id":x['service'],"name":x["name"], "type":x["type"], "rate":x["rate"], "min":x["min"], "max":x["max"]})

        return data

    def view_services(self):
        return view_services(self.API_KEY,self.API_URL,self.headers)

    def view_categories(self):
        return view_categorys(self.API_KEY,self.API_URL,self.headers)

    def user_balance(self):
        data = {'key':self.API_KEY, 'action':'balance'}
        resp = requests.post(self.API_URL,data=data).json()
        return resp

api_star_lumiere = star_lumiere()

#print(api_star_lumiere.view_categories())

#print(api_star_lumiere.view_service(("15077","15493")))

#print(api_star_lumiere.user_balance())