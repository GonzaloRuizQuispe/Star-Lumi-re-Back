from libs.database_c import database_api
from libs.star_lumiere.star_lumire import api_star_lumiere

#Devolver Datos De Los Servicios
def view_services(name):
    resp = api_star_lumiere.view_services()
    
    data = []

    for x in resp:
        if x['category'] == name:
            data.append(x)

    #Se Retorna El Mensaje Con Su Status
    return data

