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
@app.route('/login',methods=['POST'])
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

#API Login verify
@app.route('/verify',methods=['POST'])
def verify():
    try:

        #Se Recolecta El Archivo JSON
        data = request.json

        #Se Utiliza La Funcion Login Por Token Header
        result = users_and_admins.login_token_header(data['token_header'])

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

#API Category 1 (Mostrar O Agregar Categorias De Plataformas)
@app.route('/category_plataform',methods=['GET','POST'])
def category_plataform():
    try:
        
        #Si El Metodo Es GET Se Retornan Todas Las Categorias
        if request.method == 'GET':
            
            #Se Retornan Las Categorias Sin Necesidad De Datos
            return (orders_and_receipt.view_category_plataform())
        
        #Si El Metodo Es POST Se Procede A Agregar Una Categoria De Plataforma
        if request.method == 'POST':
            
            #Se Recolectan El Archivo JSON
            data = request.json

            #Se Agrega La Categoria Plataforma A La DB Y Se Retorna El Mensaje
            return orders_and_receipt.add_category_plataform(data['name'])

    except Exception as e:

        #Se Extrae La Fecha Actual
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtiene la fecha y hora actual
        
        #Se Genera El Mensaje De Error
        mensaje_error = f'{fecha_actual} - Se ha producido un error en /category_plataform: {str(e)}\n'

        #Se guarda En Un Archivo Llamado errores.txt
        with open('errores.txt', 'a') as archivo: archivo.write(mensaje_error)
        
        #Se Retorna Error De Procesamiento Para La Web
        return users_and_admins.message_return({"message":"server internal error"},500)

#API Category 2 (Mostrar O Agregar Categorias De Servicios)
@app.route('/category_service',methods=['GET','POST'])
def category_service():
    try:
        
        #Si El Metodo Es GET Se Retornan Todas Las Categorias
        if request.method == 'GET':
            
            #Se Retornan Las Categorias Sin Necesidad De Datos
            return (orders_and_receipt.view_category_service())
        
        #Si El Metodo Es POST Se Procede A Agregar Una Categoria De Plataforma
        if request.method == 'POST':
            
            #Se Recolectan El Archivo JSON
            data = request.json

            #Se Agrega La Categoria Plataforma A La DB
            result = orders_and_receipt.add_category_service(data['name'],data['id_c_plataform'])

            #Se Retorna El Mensaje
            return (result)

    except Exception as e:

        #Se Extrae La Fecha Actual
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtiene la fecha y hora actual
        
        #Se Genera El Mensaje De Error
        mensaje_error = f'{fecha_actual} - Se ha producido un error en /category_service: {str(e)}\n'

        #Se guarda En Un Archivo Llamado errores.txt
        with open('errores.txt', 'a') as archivo: archivo.write(mensaje_error)
        
        #Se Retorna Error De Procesamiento Para La Web
        return users_and_admins.message_return({"message":"server internal error"},500)

#API Services (Mostrar Servicios)
@app.route('/service',methods=['GET','POST'])
def service():
    try:
        
        #Si El Metodo Es GET Se Retornan Todas Las Categorias
        if request.method == 'GET':
            
            #Se Retornan Las Categorias Sin Necesidad De Datos
            return (orders_and_receipt.view_services(data['id_c_service']))
        
        #Si El Metodo Es POST Se Procede A Agregar Una Categoria De Plataforma
        if request.method == 'POST':
            
            #Se Recolectan El Archivo JSON
            data = request.json
            
            #Se Agrega La Categoria Plataforma A La DB Y Se Retorna El Mensaje
            return orders_and_receipt.add_service(data['id_c_service'],data['name'],data['description'],data['type'],data['min'],data['max'],data['rate_o'])

    except Exception as e:

        #Se Extrae La Fecha Actual
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtiene la fecha y hora actual
        
        #Se Genera El Mensaje De Error
        mensaje_error = f'{fecha_actual} - Se ha producido un error en /service: {str(e)}\n'

        #Se guarda En Un Archivo Llamado errores.txt
        with open('errores.txt', 'a') as archivo: archivo.write(mensaje_error)
        
        #Se Retorna Error De Procesamiento Para La Web
        return users_and_admins.message_return({"message":"server internal error"},500)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)