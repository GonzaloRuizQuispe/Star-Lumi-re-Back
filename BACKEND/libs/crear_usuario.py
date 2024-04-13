from libs.database_c import database_api
from libs.gen_tokens import tokens_api

def crear_usuario_api(username,password,email): # Crear Usuario En La DB
        
        resp_0 = database_api.control_db("SELECT * FROM Usuarios WHERE BINARY email='{}'".format(email),"Automatic - Consult Email Exists") #Consultar Si Existe El Correo

        if not resp_0: # Si La Lista Esta Vacia Se Accede
            
            token_header = tokens_api.gen_token_header() # Generar Token Header, Identificador Web
            token_acceso = tokens_api.gen_token_acceso() # Generar Token A2F De Acceso

            resp_1 = database_api.control_db("INSERT INTO Usuarios (username,password,email,token_header,token_acceso) VALUES ('{}','{}','{}','{}','{}')".format(username,password,email,token_header,token_acceso),"Automatic - Created User") #Se Guardan Los Datos

            return database_api.message_return("user created",201)

        else: # Si La Lista No Esta Vacia
            
            return database_api.message_return("email exists",400)