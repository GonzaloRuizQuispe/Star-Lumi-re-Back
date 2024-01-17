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

    def user_balance(self):
        data = {'key':self.API_KEY, 'action':'balance'}
        resp = requests.post(self.API_URL,data=data)
        return resp.json()

api_star_lumiere = star_lumiere()