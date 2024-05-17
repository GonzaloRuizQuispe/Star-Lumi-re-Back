from libs.database_c import database_api

def change_c_service(id_service,id_c_service):
    return database_api.control_db("UPDATE Service SET id_c_service='{}' WHERE id='{}'".format(id_c_service,id_service))