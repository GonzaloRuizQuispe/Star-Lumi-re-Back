import requests
from dotenv import load_dotenv
import os
from orders_receipt_db import orders_and_receipt

class star_lumiere():

    #Cargar Datos De .env
    load_dotenv()

    #Key Para Vincular A La Cuenta Original
    API_KEY = os.getenv("API_KEY") #SMM ENGINER

    #Link Que Conecta Con La API
    API_URL = os.getenv("API_URL") #SMM ENGINER

    #En Cabezado Para Evitar Errores
    headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)'}

    #Servicios Filtrados Por Categoria
    def view_category(self,category):

        #Se Llena La Accion A Realizar
        data = {'key':self.API_KEY, 'action':'services'}

        #Se Hace La Consulta
        resp = requests.post(self.API_URL,data=data).json()

        #Se Filtra Segun La Categoria Deseada
        filtered_data = [item for item in resp if item['category'] == category]

        #Se Retorna El Mensaje
        return filtered_data

    def view_service(self):

        #Se Llena La Accion A Realizar
        data = {'key':self.API_KEY, 'action':'services'}

        #Se Hace La Consulta
        resp = requests.post(self.API_URL,data=data).json()

        return resp

    def user_balance(self):
        data = {'key':self.API_KEY, 'action':'balance'}
        resp = requests.post(self.API_URL,data=data).json()
        return resp

api_star_lumiere = star_lumiere()

#print(api_star_lumiere.user_balance())

#resp = (api_star_lumiere.view_category("New 🔥 | Instagram Services")[0])

#print(api_star_lumiere.view_service()[0])

#orders_and_receipt.add_service(resp['service'],"1",resp['name'],"",resp['type'],resp['min'],resp['max'],resp['rate'])
