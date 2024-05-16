from libs.database_c import database_api

#Agregar Servicios
def add_service(id_original,id_c_service,description):
    
    resp = database_api.control_db("SELECT * FROM Service WHERE id_original='{}'".format(id_original))

    #Se Verifica Que No Exista El Servicio
    if not resp:

        resp_1 = database_api.control_db("INSERT INTO Service (id_original,id_c_service,description) VALUES ('{}','{}','{}')".format(id_original,id_c_service,description))

        #Se Retorna Un Mensaje Notificando
        return "201 creado"

    #Caso Contrario Se Notifica Que Ya Existe
    else:

        #Se Retorna Un Mensaje Notificando
        return "400 Ya Existe resp[0][0]"