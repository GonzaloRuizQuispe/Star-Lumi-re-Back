from libs.database_c import database_api
from libs.star_lumiere.star_lumire import api_star_lumiere

#Devolver Datos De Los Servicios
def view_services(id_c_service):
    resp = database_api.control_db("SELECT * FROM Service WHERE id_c_service='{}'".format(id_c_service))
    ids = []
    #Creamos Una Variable Recursiva   
    for x in resp:
        ids.append(x[1])

    resp_1 = api_star_lumiere.view_service_ids(ids)

    #Se Retorna El Mensaje Con Su Status
    return resp_1

