from database import database_api

def login_header_api(token_header):
    resp_0 = database_api.control_db("SELECT * FROM Usuarios WHERE BINARY token_header='{}'".format(token_header),"Automatic - Consult Token_Header") #Se Consulta Si Existe El Token_Header

    if resp_0: # Si Existe
        return resp_0

    else: # Si No Existe
        return "No Existe"