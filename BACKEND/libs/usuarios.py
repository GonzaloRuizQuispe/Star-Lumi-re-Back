from database import database_api

from crear_usuario import crear_usuario_api
from login_email import login_email_api
from login_header import login_header_api
from cambiar_email import cambiar_email_api

class Usuarios():

    def crear_usuario(self,username,password,email):
        return crear_usuario_api(username,password,email)

    def login_email(self,email,password):
        return login_email_api(email,password)

    def login_header(self,token_header):
        return login_header_api(token_header)

    def cambiar_email(self,id,new_email):
        return cambiar_email_api(id,new_email)

    def cambiar_contraseña():
        pass

    def cambiar_balance():
        pass

    def activar_desactivar_a2f():
        pass

usuarios_api = Usuarios()

print(usuarios_api.cambiar_email(1,"Chacha@Gmail.com"))