from libs.database_c import database_api

def login_email_api(email,password):
    
    resp_0 = database_api.control_db("SELECT * FROM Usuarios WHERE BINARY email='{}'".format(email),"Automatic - Consult Email Login") # Consultar Si Existe El Email

    if resp_0: # Si Existe

        resp_1 = database_api.control_db("SELECT * FROM Usuarios WHERE BINARY email='{}' AND BINARY password='{}'".format(email,password),"Automatic - Consult Email And Password Login") # Consultar Si Existe El Email Con Contraseña

        if resp_1: #Si Existe 

            return database_api.message_return(resp_1,200)

        else: # Si No Existe

            return database_api.message_return("incorrect password",400)

    else: # Si No Existe

        return database_api.message_return("incorrect email",400)