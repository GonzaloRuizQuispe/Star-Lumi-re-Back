from libs.database_c import database_api
from libs.star_lumiere.star_lumire import api_star_lumiere

#Devolver Datos De Categoria De Servicio
def view_category_service(name):
        
    #Se Declara Una Variable Recursiva
    resp_1 = api_star_lumiere.view_categories()

    data = []

    for x in resp_1:
        if str(name).upper() in str(x).upper() and "NEW 🔥" not in str(x).upper():
                data.append({"name":x})
        if str(name).upper() in str(x).upper() and "NEW 🔥" == str(name).upper():
                data.append({"name":x})

    #Se Retorna El Mensaje Con Su Status
    return data