from libs.database_c import database_api

def login_email_api(email,password):
    
    resp_0 = database_api.control_db("SELECT * FROM Usuarios WHERE BINARY email='{}'".format(email),"Automatic - Consult Email Login") # Consultar Si Existe El Email

    if resp_0: # Si Existe

        resp_1 = database_api.control_db("SELECT * FROM Usuarios WHERE BINARY email='{}' AND BINARY password='{}'".format(email,password),"Automatic - Consult Email And Password Login") # Consultar Si Existe El Email Con Contraseña

        if resp_1: #Si Existe 

            data = []

            for id,username,password,email,token_header,token_acceso,rol,balance,a2f in resp_1:
                data.append({"id":id,"username":username,"password":password,"email":email,"token_header":token_header,"token_acceso":token_acceso,"rol":rol,"balance":balance,"a2f":a2f})

            return database_api.message_return(data,200)

        else: # Si No Existe

            return database_api.message_return("incorrect password",400)

    else: # Si No Existe

        return database_api.message_return("incorrect email",400)