from flask import Flask, request
from flask_cors import CORS

from libs.database_c import database_api
from libs.users.usuarios import usuarios_api
from libs.services.services import services_api

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


############################

#API Category 1 (Mostrar)
@app.route('/category_plataforms',methods=['GET'])
def category_plataform():
    try:

        #Se Retornan Las Categoryas Plataform Disponibles
        return services_api.view_category_plataform()

    except Exception as e:
        
        database_api.logs("{}".format(e),"Automatic - /category_plataforms")

        return database_api.message_return("Error Internal 500 Verify",500)

#API Category 2 (Mostrar)
@app.route('/category_services',methods=['POST'])
def category_service():
    try:

        #Se Recolecta El JSON
        data = request.json

        #Se Retornan Las Categorias Pertenecientes A La Plataforma
        return (services_api.view_category_service(data['id_c_plataform']))

    except Exception as e:

        database_api.logs("{}".format(e),"Automatic - /category_services")

        return database_api.message_return("Error Internal 500 Verify",500)

#API Services (Mostrar Servicios)
@app.route('/services',methods=['POST'])
def service():
    try:
        
        data = request.json
        
        return services_api.view_services(data['id_c_service'])

    except Exception as e:

        database_api.logs("{}".format(e),"Automatic - /services")

        return database_api.message_return("Error Internal 500 Verify",500)

#API Add Category Plataform
@app.route('/add_category_plataform',methods=['POST'])
def add_category_plataform():
    try:
        
        data = request.json

        return services_api.add_category_plataform(data['name'])

    except Exception as e:

        database_api.logs("{}".format(e),"Automatic - /add_category_plataform")

        return database_api.message_return("Error Internal 500 Verify",500)

#API Add Category Service
@app.route('/add_category_service',methods=['POST'])
def add_category_service():
    try:
        
        data = request.json

        return services_api.add_category_service(data['name'],data['id_c_plataform'])

    except Exception as e:

        database_api.logs("{}".format(e),"Automatic - /add_category_service")

        return database_api.message_return("Error Internal 500 Verify",500)

#API Orders
@app.route('/orders',methods=['POST'])
def orders():
    try:
        data = request.json

        database_api.logs(str(data),"TEST 3")

        services_api.add_orders(data['id_user'],data['link'],data['price_final'],data['quantity'],data['id_service'],data['type'],data['balance'])

        return "Funciona"

    except Exception as e:

        database_api.logs("{}".format(e),"Automatic - /orders")

        return database_api.message_return("Error Internal 500 Verify",500)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)