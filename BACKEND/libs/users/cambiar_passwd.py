from libs.database_c import database_api

def cambiar_passwd(id,old_passwd,new_passwd):
    resp = database_api.control_db("SELECT * FROM Usuarios WHERE id='{}'".format(id))

    if resp[0][2] == old_passwd:
        resp_1 = database_api.control_db("UPDATE Usuarios SET password='{}' WHERE id='{}'".format(new_passwd,id))
        return "Valid"
    else:
        return "Old Psswd Incorrect"