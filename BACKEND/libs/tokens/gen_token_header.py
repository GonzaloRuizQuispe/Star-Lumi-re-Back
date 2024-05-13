import pyotp
from libs.database_c import database_api

#Generar Token Header Para Los Usuarios/Administradores
def gen_token_header():

    #Se Genera El Token
    token = pyotp.random_base32(length=64)

    resp = database_api.control_db((f"SELECT * FROM Usuarios WHERE token_header = '{token}'"))

    #De No Hallar Similitud Se Retorna La Cadena
    if not resp:
        return token
    #Caso Contrario Se Vuelve A Ejecutar La Funcion
    else:
        return gen_token_header()