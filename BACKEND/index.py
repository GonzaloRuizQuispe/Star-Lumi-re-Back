from flask import Flask, request, jsonify
from flask_cors import CORS
from libs.users_admins_db import database
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
        result = database.agregar_user(data['username'],data['password'],data['email'],data['token_header'],data['token_acceso'])

        #Se Retorna El Resultado De La Funcion De La DB
        return jsonify(result)

    #Si Se Agarra Algun Error Se Almacena Para Su Posterior Fix
    except Exception as e:

        #Se Extrae La Fecha Actual
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtiene la fecha y hora actual
        
        #Se Genera El Mensaje De Error
        mensaje_error = f'{fecha_actual} - Se ha producido un error: {str(e)}\n'

        #Se guarda En Un Archivo Llamado errores.txt
        with open('errores.txt', 'a') as archivo: archivo.write(mensaje_error)
        
        #Se Retorna Error De Procesamiento Para La Web
        return jsonify({'Resultado':'Error 404'})

#API Login
@app.route('/login',methods=['GET'])
def login():
    try:

        #Se Recolecta El Archivo JSON
        data = request.json

        #Se Utiliza La Funcion Login Por Email Y Password
        result = database.login_email_pass(data['email',data['password']])

        #Se Retorna El Resultado De La Funcion
        return jsonify(result)

        

    except Exception as e:

        #Se Extrae La Fecha Actual
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtiene la fecha y hora actual
        
        #Se Genera El Mensaje De Error
        mensaje_error = f'{fecha_actual} - Se ha producido un error: {str(e)}\n'

        #Se guarda En Un Archivo Llamado errores.txt
        with open('errores.txt', 'a') as archivo: archivo.write(mensaje_error)
        
        #Se Retorna Error De Procesamiento Para La Web
        return jsonify({'Resultado':'Error 404'})

#API Login Maintain
@app.route('/maintain',methods=['GET'])
def maintain():
    try:

        #Se Recolecta El Archivo JSON
        data = request.json

        #Se Utiliza La Funcion Login Por Token Header
        result = database.login_token_header(data['Token Header'])

        #Se Retornar El Resultado De La Función
        return jsonify(result)

    except Exception as e:

        #Se Extrae La Fecha Actual
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtiene la fecha y hora actual
        
        #Se Genera El Mensaje De Error
        mensaje_error = f'{fecha_actual} - Se ha producido un error: {str(e)}\n'

        #Se guarda En Un Archivo Llamado errores.txt
        with open('errores.txt', 'a') as archivo: archivo.write(mensaje_error)
        
        #Se Retorna Error De Procesamiento Para La Web
        return jsonify({'Resultado':'Error 404'})

#API Category 1 (Seleccionar Plataforma)
@app.route('/category_plataform',methods=['GET'])
def category_1():
    try:
        pass
    except Exception as e:

        #Se Extrae La Fecha Actual
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtiene la fecha y hora actual
        
        #Se Genera El Mensaje De Error
        mensaje_error = f'{fecha_actual} - Se ha producido un error: {str(e)}\n'

        #Se guarda En Un Archivo Llamado errores.txt
        with open('errores.txt', 'a') as archivo: archivo.write(mensaje_error)
        
        #Se Retorna Error De Procesamiento Para La Web
        return jsonify({'Resultado':'Error 404'})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)