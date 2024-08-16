import pyotp
from libs.database_c import database_api

def gen_token_acceso():

    #Se Genera El Token
    token = pyotp.random_base32(length=32)

    resp = database_api.control_db((f"SELECT * FROM usuarios WHERE token_acceso = '{token}'"))
    #De No Hallar Similitud Se Retorna La Cadena
    if not resp:
        return token
    #Caso Contrario Se Vuelve A Ejecutar La Funcion
    else:
        return gen_token_acceso()

