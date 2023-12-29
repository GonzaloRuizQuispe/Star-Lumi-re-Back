import requests

class star_lumiere():
    
    #Key Para Vincular A La Cuenta Original
    API_KEY = "7b08dd9f72cc704ffb1d3e74997df7ff" #SMM ENGINER

    #Link Que Conecta Con La API
    API_URL = "https://smmengineer.com/api/v2" #SMM ENGINER

    #En Cabezado Para Evitar Errores
    headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)'}

    def user_balance(self):
        data = {'key':self.API_KEY, 'action':'balance'}
        resp = requests.post(self.API_URL,data=data)
        return resp.json()

api_star_lumiere = star_lumiere()