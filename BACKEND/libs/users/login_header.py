from libs.database_c import database_api

def login_header_api(token_header):
    resp_0 = database_api.control_db("SELECT * FROM Usuarios WHERE BINARY token_header='{}'".format(token_header)) #Se Consulta Si Existe El Token_Header

    if resp_0: # Si Existe

        data = []

        for id,username,password,email,token_header,token_acceso,rol,balance,a2f in resp_0:

            data.append({"id":id,"username":username,"email":email,"token_header":token_header,"token_acceso":token_acceso,"rol":rol,"balance":balance,"a2f":a2f})

        return database_api.message_return(data[0],200)

    else: # Si No Existe
        return database_api.message_return("token_header invalid",400)