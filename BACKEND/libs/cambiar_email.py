from libs.database_c import database_api

def cambiar_email_api(id,new_email):

    resp_0 = database_api.control_db("UPDATE Usuarios SET email = '{}' WHERE id='{}'".format(new_email,id),"Automatic - Change Email")