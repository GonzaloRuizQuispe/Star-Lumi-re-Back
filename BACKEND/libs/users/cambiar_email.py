from libs.database_c import database_api

def cambiar_email_api(id,old_email,new_email):
    resp = database_api.control_db("SELECT * FROM Usuarios WHERE id='{}'".format(id))

    if resp[0][3] == old_email:
        resp_1 = database_api.control_db("UPDATE Usuarios SET email='{}' WHERE id='{}'".format(new_email,id))
        return "Valid"
    else:
        return "Old Email Incorrect"