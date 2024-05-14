from libs.database_c import database_api

def cambiar_balance(old_balance,price,id):

    new_balance = old_balance-price

    resp = database_api.control_db("UPDATE Usuarios SET balance='{}' WHERE id='{}'".format(new_balance,id))