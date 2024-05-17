from libs.database_c import database_api

def change_description(id_service,description):
    
    return database_api.control_db("UPDATE Service SET description='{}' WHERE id='{}'".format(description,id_service))