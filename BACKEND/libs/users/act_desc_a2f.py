from libs.database_c import database_api

def act_desc_a2f(id):
    resp = database_api.control_db("SELECT * FROM Usuarios WHERE id='{}'".format(id))

    if resp[0][8] == 0:
        resp_1 = database_api.control_db("UPDATE Usuarios SET a2f='1' WHERE id='{}'".format(id))

    elif resp[0][8] == 1:
        resp_1 = database_api.control_db("UPDATE Usuarios SET a2f='0' WHERE id='{}'".format(id))

    else:
        resp_1 = "Account Invalid"

    return resp_1