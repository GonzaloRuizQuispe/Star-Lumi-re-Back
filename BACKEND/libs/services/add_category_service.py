from libs.database_c import database_api

#Agregar Categoria De Servicio
def add_category_service(name,id_c_plataform):
        
    resp = database_api.control_db("SELECT * FROM C_Service WHERE name='{}'".format(name))

    #Se Verifica Que No Exista La Categoria En La DB
    if not resp:

        resp_1 = database_api.control_db("INSERT INTO C_Service (name,id_c_plataform) VALUES ('{}','{}')".format(name,id_c_plataform))

        #Se Retorna Un Mensaje Notificando
        return "201 Creado"

    #Caso Contrario Se Retorna Que Existe La Categoria Con ID
    else:
            
        #Se Retorna Un Mensaje Notificando
        return "400 Ya Existe resp[0][0]"
