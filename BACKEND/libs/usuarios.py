from libs.crear_usuario import crear_usuario_api
from libs.login_email import login_email_api
from libs.login_header import login_header_api
from libs.cambiar_email import cambiar_email_api

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