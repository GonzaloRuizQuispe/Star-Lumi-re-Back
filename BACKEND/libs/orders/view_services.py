from libs.database_c import database_api

#Devolver Datos De Los Servicios
def view_services(id_c_service):
    
    resp = database_api.control_db("SELECT * FROM Service WHERE id_c_service={}".format(id_c_service))

    #Creamos Una Variable Recursiva
    data = []
        
    #Se Crea El JSON
    for id, id_original, id_c_service, description in resp:
            
        #Se Agrega A La Lista
        data.append({"id":f"{id}","id_original":f"{id_original}","id_c_service":f"{id_c_service}","description":f"{description}"})

    #Se Retorna El Mensaje Con Su Status
    return data