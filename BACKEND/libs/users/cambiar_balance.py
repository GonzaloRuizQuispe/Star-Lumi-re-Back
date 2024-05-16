from libs.database_c import database_api

def cambiar_balance(new_balance,id):

    resp = database_api.control_db("UPDATE Usuarios SET balance='{}' WHERE id='{}'".format(new_balance,id))