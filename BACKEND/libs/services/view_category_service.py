from libs.database_c import database_api
from libs.star_lumiere.star_lumire import api_star_lumiere

#Devolver Datos De Categoria De Servicio
def view_category_service(id_c_plataform):
        
    resp = database_api.control_db("SELECT * FROM C_Plataform WHERE id='{}'".format(id_c_plataform))

    #Se Declara Una Variable Recursiva
    resp_1 = api_star_lumiere.view_categories()

    data = []

    for x in resp_1:
        if resp[0][1] != 1:
            if str(resp[0][1]).upper() in str(x).upper() and "NEW 🔥" not in str(x).upper():
                data.append({"name":x})
        elif resp[0][1] == 1:
            if str(resp[0][1]).upper() in str(x).upper():
                data.append({"name":x})

    #Se Retorna El Mensaje Con Su Status
    return data