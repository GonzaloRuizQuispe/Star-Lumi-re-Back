from libs.database_c import database_api

#Agregar Categoria De Plataforma
def add_category_plataform(name):
    
    resp = database_api.control_db("SELECT * FROM C_Plataform WHERE name='{}'".format(name))

    #Se Verifica Que No Exista La Categoria En La DB
    if not resp:

        resp_1 = database_api.control_db("INSERT INTO C_Plataform (name) VALUES ('{}')".format(name))

        #Se Retorna Un Mensaje Notificando
        return "201 Creado"

    #Caso Contrario Se Retorna Que Existe La Categoria Con ID
    else:

        #Se Retorna Un Mensaje Notificando
        return "400 Ya Existe ID resp[0][0]"