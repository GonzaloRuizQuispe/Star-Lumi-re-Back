from libs.database_c import database_api

#Devolver Datos De Categoria De Plataforma
def view_category_plataform():
        
    resp = database_api.control_db("SELECT * FROM C_Plataform")

    #Variable Provicional
    data = []

    #Se Arma El JSON Iterando Los Objetos
    for id, name in resp:

        #Se Agrega A La Lista
        data.append({"name":f"{name}"})

    #Se Retorna El Mensaje Con Su Status
    return data