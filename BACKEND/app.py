from flask import Flask, request
from flask_cors import CORS

#from libs.orders_receipt_db import orders_and_receipt
#from libs.star_lumire import api_star_lumiere

from libs.usuarios import usuarios_api
from libs.database_c import database_api

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

    try:
        data = request.json # Se Recolecta El Archivo JSON

        result = usuarios_api.crear_usuario(data['username'],data['password'],data['email']) # Se Envian Los Datos Para Su Registro

        return result

    except Exception as e: # Si Rompe De Alguna Forma Se Guarda El Porque
        database_api.logs("{}".format(e),"Automatic - /Register")

        return database_api.message_return("Error Internal 500 Register",500)

 #API Login
@app.route('/login',methods=['POST'])
def login(): 

    try:
        data = request.json # Se Recolecta El Archivo JSON

        result = usuarios_api.login_email(data['email'],data['password'])

        return result
    
    except Exception as e:
        database_api.logs("{}".format(e),"Automatic - /Login")
        
        return database_api.message_return("Error Internal 500 Login",500)

#API Login verify
@app.route('/verify',methods=['POST'])
def verify():
    try:
        data = request.json

        result = usuarios_api.login_header(data['token_header'])

        return result

    except Exception as e:
        database_api.logs("{}".format(e),"Automatic - /verify")

        return database_api.message_return("Error Internal 500 Verify",500)


"""
#API Category 1 (Mostrar)
@app.route('/category_plataforms',methods=['GET'])
def category_plataform():
    try:

        #Se Retornan Las Categoryas Plataform Disponibles
        return orders_and_receipt.view_category_plataform()

    except Exception as e:

        #Se Extrae La Fecha Actual
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtiene la fecha y hora actual
        
        #Se Genera El Mensaje De Error
        mensaje_error = f'{fecha_actual} - Se ha producido un error en /category_plataform: {str(e)}\n'

        #Se guarda En Los Registros De La DB
        database.save_logs(mensaje_error)
        
        #Se Retorna Error De Procesamiento Para La Web
        return orders_and_receipt.message_return({"message":"server internal error"},500)

#API Category 2 (Mostrar)
@app.route('/category_services',methods=['POST'])
def category_service():
    try:

        #Se Recolecta El JSON
        data = request.json

        #Se Retornan Las Categorias Pertenecientes A La Plataforma
        return (orders_and_receipt.view_category_service(data['id_c_plataform']))

    except Exception as e:

        #Se Extrae La Fecha Actual
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtiene la fecha y hora actual
        
        #Se Genera El Mensaje De Error
        mensaje_error = f'{fecha_actual} - Se ha producido un error en /category_service: {str(e)}\n'

        #Se guarda En Los Registros De La DB
        database.save_logs(mensaje_error)
        
        #Se Retorna Error De Procesamiento Para La Web
        return orders_and_receipt.message_return({"message":"server internal error"},500)

#API Services (Mostrar Servicios)
@app.route('/services',methods=['POST'])
def service():
    try:
        
        data = request.json

        return orders_and_receipt.view_services(data['id_c_service'])

    except Exception as e:

        #Se Extrae La Fecha Actual
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtiene la fecha y hora actual
        
        #Se Genera El Mensaje De Error
        mensaje_error = f'{fecha_actual} - Se ha producido un error en /service: {str(e)}\n'

        #Se guarda En Los Registros De La DB
        database.save_logs(mensaje_error)
        
        #Se Retorna Error De Procesamiento Para La Web
        return orders_and_receipt.message_return({"message":"server internal error"},500)

#API Add Category Plataform
@app.route('/add_category_plataform',methods=['POST'])
def add_category_plataform():
    try:
        
        data = request.json

        return orders_and_receipt.add_category_plataform(data['name'])

    except Exception as e:

        #Se Extrae La Fecha Actual
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtiene la fecha y hora actual
        
        #Se Genera El Mensaje De Error
        mensaje_error = f'{fecha_actual} - Se ha producido un error en /add_category_plataform: {str(e)}\n'

        #Se guarda En Los Registros De La DB
        database.save_logs(mensaje_error)
        
        #Se Retorna Error De Procesamiento Para La Web
        return orders_and_receipt.message_return({"message":"server internal error"},500)

#API Add Category Service
@app.route('/add_category_service',methods=['POST'])
def add_category_service():
    try:
        
        data = request.json

        return orders_and_receipt.add_category_service(data['name'],data['id_c_plataform'])

    except Exception as e:

        #Se Extrae La Fecha Actual
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtiene la fecha y hora actual
        
        #Se Genera El Mensaje De Error
        mensaje_error = f'{fecha_actual} - Se ha producido un error en /add_category_service: {str(e)}\n'

        #Se guarda En Los Registros De La DB
        database.save_logs(mensaje_error)
        
        #Se Retorna Error De Procesamiento Para La Web
        return orders_and_receipt.message_return({"message":"server internal error"},500)

#API Verify OTP DB
@app.route('/to_acces',methods=['POST'])
def to_acces():
    try:
        
        data = request.json

        return database.code_rol_validation(data['code'])

    except Exception as e:

        #Se Extrae La Fecha Actual
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtiene la fecha y hora actual
        
        #Se Genera El Mensaje De Error
        mensaje_error = f'{fecha_actual} - Se ha producido un error en /to_acces: {str(e)}\n'

        #Se guarda En Los Registros De La DB
        database.save_logs(mensaje_error)
        
        #Se Retorna Error De Procesamiento Para La Web
        return orders_and_receipt.message_return({"message":"server internal error"},500)

#API Consultas
@app.route('/consult_db',methods=['POST'])
def consult_db():
    try:
        
        data = request.json

        return database.consult_db(data['consult'])

    except Exception as e:

        #Se Extrae La Fecha Actual
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtiene la fecha y hora actual
        
        #Se Genera El Mensaje De Error
        mensaje_error = f'{fecha_actual} - Se ha producido un error en /consult_db: {str(e)}\n'
        
        #Se guarda En Los Registros De La DB
        database.save_logs(mensaje_error)
    
        #Se Retorna Error De Procesamiento Para La Web
        return orders_and_receipt.message_return({"message":"server internal error"},500)

#API Payeer
@app.route('/payeer',methods=['GET'])
def payeer():
    with open('payeer_2043637184.txt', 'r') as f:
        contenido = f.read()
    return contenido """

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)