from dotenv import load_dotenv
import os,time,threading,requests

from libs.star_lumiere.view_categories import view_categorys
from libs.star_lumiere.view_services_ids import view_services_ids

from libs.star_lumiere.orders_default import orders_default

class star_lumiere():

    #Cargar Datos De .env
    load_dotenv()

    #Key Para Vincular A La Cuenta Original
    API_KEY = os.getenv("API_KEY") #SMM ENGINER

    #Link Que Conecta Con La API
    API_URL = os.getenv("API_URL") #SMM ENGINER

    #En Cabezado Para Evitar Errores
    headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)'}

    def __init__(self):
        self.services = self.fetch_services()  # Inicializa los servicios al crear la instancia
        
        # Iniciar un hilo que actualiza los servicios cada hora
        self.update_thread = threading.Thread(target=self._update_services_periodically)
        self.update_thread.daemon = True  # Hilo en segundo plano
        self.update_thread.start()

    def fetch_services(self):
        data = {'key': self.API_KEY, 'action': 'services'}
        return requests.post(self.API_URL, data=data).json()

    def _update_services_periodically(self):
        while True:
            self.services = self.fetch_services()  # Actualiza los servicios
            print("Services updated")
            time.sleep(3600)  # Espera 1 hora (3600 segundos)

    def view_services(self):
        return self.services

    def view_categories(self):
        return view_categorys(self.services)

    def user_balance(self):
        data = {'key':self.API_KEY, 'action':'balance'}
        resp = requests.post(self.API_URL,data=data).json()
        return resp

    def orders_default(self,id_service,link,quantity):
        return orders_default(id_service,link,quantity,self.API_URL,self.API_KEY)

api_star_lumiere = star_lumiere()

#print(api_star_lumiere.view_categories())

#print(api_star_lumiere.view_service_ids(("15656")))

#print(api_star_lumiere.user_balance())