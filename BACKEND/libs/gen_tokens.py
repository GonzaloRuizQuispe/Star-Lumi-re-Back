import pyotp
from database_c import database_api

class tokens():

    #Generar Token Header Para Los Usuarios/Administradores
    def gen_token_header(self):

        #Se Genera El Token
        token = pyotp.random_base32(length=64)

        resp = database_api.control_db((f"SELECT * FROM Usuarios WHERE token_header = '{token}'"), ("Automatic - Gen Token Header"))

        #De No Hallar Similitud Se Retorna La Cadena
        if not resp:
            return token
        #Caso Contrario Se Vuelve A Ejecutar La Funcion
        else:
            return self.gen_token_header()
        
    #Generar Token Acceso Para Los Usuarios/Administradores
    def gen_token_acceso(self):

        #Se Genera El Token
        token = pyotp.random_base32(length=32)

        resp = database_api.control_db((f"SELECT * FROM Usuarios WHERE token_acceso = '{token}'"), ("Automatic - Gen Token Acceso"))

        #De No Hallar Similitud Se Retorna La Cadena
        if not resp:
            return token
        #Caso Contrario Se Vuelve A Ejecutar La Funcion
        else:
            return self.gen_token_acceso()

tokens_api = tokens()
