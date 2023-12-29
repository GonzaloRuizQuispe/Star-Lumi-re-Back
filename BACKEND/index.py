from flask import Flask, request
from flask_cors import CORS
from libs.users_admins_db import users_and_admins
from libs.orders_receipt_db import orders_and_receipt
from libs.star_lumire import api_star_lumiere
import datetime

#Se Crea La Web App
app = Flask(__name__)

#Se Configura El Cors
cors = CORS(app, resources={r"/*":{"origins":"*"}}, supports_credentials=True)
def verificar():
    pass

#Saber Si Esta Prendido
@app.route('/')
def home():
    return "<h1>El Que Usa Esta API Es Gay<h1>"

#API Registro
@app.route('/register',methods=['POST'])
def register():

    #Se Usa Try Except Para Evadir Errores
    try:

        #Se Recolecta El Archivo JSON
        data = request.json

        #Se Utiliza La Funcion De Agregar A Database
        result = users_and_admins.agregar_user(data['username'],data['password'],data['email'],data['rol'])

        #Se Retorna El Resultado De La Funcion De La DB
        return (result)

    #Si Se Agarra Algun Error Se Almacena Para Su Posterior Fix
    except Exception as e:

        #Se Extrae La Fecha Actual
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtiene la fecha y hora actual
        
        #Se Genera El Mensaje De Error
        mensaje_error = f'{fecha_actual} - Se ha producido un error en /register: {str(e)}\n'

        #Se guarda En Un Archivo Llamado errores.txt
        with open('errores.txt', 'a') as archivo: archivo.write(mensaje_error)
        
        #Se Retorna Error De Procesamiento Para La Web
        return users_and_admins.message_return({"message":"server internal error"},500)

#API Login
@app.route('/login',methods=['GET'])
def login():
    try:

        #Se Recolecta El Archivo JSON
        data = request.json

        #Se Utiliza La Funcion Login Por Email Y Password
        result = users_and_admins.login_email_pass(data['email'],data['password'])

        #Se Retorna El Resultado De La Funcion
        return (result)

        

    except Exception as e:

        #Se Extrae La Fecha Actual
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtiene la fecha y hora actual
        
        #Se Genera El Mensaje De Error
        mensaje_error = f'{fecha_actual} - Se ha producido un error en /login: {str(e)}\n'

        #Se guarda En Un Archivo Llamado errores.txt
        with open('errores.txt', 'a') as archivo: archivo.write(mensaje_error)
        
        #Se Retorna Error De Procesamiento Para La Web
        return users_and_admins.message_return({"message":"server internal error"},500)

#API Login Maintain
@app.route('/maintain',methods=['GET'])
def maintain():
    try:

        #Se Recolecta El Archivo JSON
        data = request.json

        #Se Utiliza La Funcion Login Por Token Header
        result = users_and_admins.login_token_header(data['Token Header'])

        #Se Retornar El Resultado De La Función
        return (result)

    except Exception as e:

        #Se Extrae La Fecha Actual
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtiene la fecha y hora actual
        
        #Se Genera El Mensaje De Error
        mensaje_error = f'{fecha_actual} - Se ha producido un error en /maintain: {str(e)}\n'

        #Se guarda En Un Archivo Llamado errores.txt
        with open('errores.txt', 'a') as archivo: archivo.write(mensaje_error)
        
        #Se Retorna Error De Procesamiento Para La Web
        return users_and_admins.message_return({"message":"server internal error"},500)

#API Category 1 (Seleccionar Plataforma)
@app.route('/category_plataform',methods=['GET'])
def category_1():
    try:
        pass
    except Exception as e:

        #Se Extrae La Fecha Actual
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtiene la fecha y hora actual
        
        #Se Genera El Mensaje De Error
        mensaje_error = f'{fecha_actual} - Se ha producido un error en /category_plataform: {str(e)}\n'

        #Se guarda En Un Archivo Llamado errores.txt
        with open('errores.txt', 'a') as archivo: archivo.write(mensaje_error)
        
        #Se Retorna Error De Procesamiento Para La Web
        return users_and_admins.message_return({"message":"server internal error"},500)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)