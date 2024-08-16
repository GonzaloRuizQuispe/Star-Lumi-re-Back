from libs.database_c import database_api
from libs.tokens.gen_tokens import tokens_api

def crear_usuario_api(username, password, email):  # Crear Usuario En La DB

    # Consulta parametrizada para evitar inyecciones SQL
    resp_0 = database_api.control_db("SELECT * FROM Usuarios WHERE email = %s", (email,))  # Consultar Si Existe El Correo

    if not resp_0:  # Si La Lista Está Vacía, Se Accede

        token_header = tokens_api.gen_token_header()  # Generar Token Header, Identificador Web
        token_acceso = tokens_api.gen_token_acceso()  # Generar Token A2F De Acceso

        # Consulta segura utilizando parámetros
        resp_1 = database_api.control_db(
            "INSERT INTO Usuarios (username, password, email, token_header, token_acceso) VALUES (%s, %s, %s, %s, %s)",
            (username, password, email, token_header, token_acceso)
        )  # Se Guardan Los Datos

        return database_api.message_return("user created", 201)

    else:  # Si La Lista No Está Vacía
        return database_api.message_return("email exists", 400)
