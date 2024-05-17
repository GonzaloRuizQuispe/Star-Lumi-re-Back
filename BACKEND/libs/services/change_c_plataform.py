from libs.database_c import database_api

def change_c_plataform(id_c_service,id_c_plataform):
    return database_api.control_db("UPDATE C_Service SET id_c_plataform='{}' WHERE id='{}'".format(id_c_plataform,id_c_service))