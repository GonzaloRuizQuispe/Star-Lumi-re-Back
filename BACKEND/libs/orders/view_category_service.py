from libs.database_c import database_api

#Devolver Datos De Categoria De Servicio
def view_category_service(self,id_c_plataform):
        
    resp = database_api.control_db("SELECT * FROM C_Service WHERE id_c_plataform='{}'".format(id_c_plataform))

    #Se Declara Una Variable Recursiva
    data = []

    #Se Arma El JSON Iterando Los Objetos
    for id,id_c_plataforms,name in resp:

        #Se Agrega A La Lista
        data.append({"id":f"{id}","id_c_plataform":f"{id_c_plataforms}","name":f"{name}"})

    #Se Retorna El Mensaje Con Su Status
    return data