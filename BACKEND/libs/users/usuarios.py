from libs.users.crear_usuario import crear_usuario_api
from libs.users.login_email import login_email_api
from libs.users.login_header import login_header_api
from libs.users.cambiar_email import cambiar_email_api
from libs.users.cambiar_balance import cambiar_balance
from libs.users.cambiar_passwd import cambiar_passwd
from libs.users.act_desc_a2f import act_desc_a2f

class Usuarios():

    def crear_usuario(self,username,password,email):
        return crear_usuario_api(username,password,email)

    def login_email(self,email,password):
        return login_email_api(email,password)

    def login_header(self,token_header):
        return login_header_api(token_header)

    def cambiar_email(self,id,old_email,new_email):
        return cambiar_email_api(id,old_email,new_email)

    def cambiar_contraseña(self,id,old_passwd,new_passwd):
        return cambiar_passwd(id,old_passwd,new_passwd)

    def cambiar_balance(self,new_balance,id):
        return cambiar_balance(new_balance,id)

    def activar_desactivar_a2f(self,id):
        return act_desc_a2f(id)

usuarios_api = Usuarios()