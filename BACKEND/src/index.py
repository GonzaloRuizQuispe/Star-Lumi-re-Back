from flask import Flask, request, jsonify
from flask_cors import CORS
from Lib.database.sql import database
from Lib.database.sql_add_user import add_user
from Lib.database.gen_token import gen_token
from Lib.database.sql_get_user_pass import get_user_pass
from Lib.database.sql_get_user_token import get_user_token
from Lib.database.execute_code import execute_code_py

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

    #Se Recolecta El Archivo Json
    data = request.json

    #Se Agrega El Usuario Mediante Add_User Guarda El Resultado De Respuesta En Resp
    resp = add_user(str(data['username']),str(data['password']),str(data['email']),str(data['phone_number']),gen_token(database),database)

    #Se Retorna En Formato Json
    return jsonify(resp)

#API Login
@app.route('/login',methods=['POST','GET'])
def login():

    #Si El Metodo De Entrada Es Post
    if request.method == 'POST':

        #Se Recolecta El Archivo Json
        data = request.json

        #Se Utilizan Los Datos Para Certificar Un Token
        token = get_user_pass(str(data['username']),str(data['password']),database)

        #Se Retorna En Formato Json
        return jsonify({'token':token})

    #Si El Metodo De Entrada Es Get
    elif request.method == 'GET':

        #Se Recolecta El Archivo Json
        data = request.json

        #Se Utiliza El Dato Para Certificar Una Cuenta Existente
        resp = get_user_token(str(data['token']),database)

        #Se Retorna En Formato Json
        return jsonify(resp)

#API Read Code
@app.route('/execute_code_py',methods=['GET'])
def executeCodePy():

    #Se Recoelcta El Archivo Json Con La Información
    data = request.json

    #Se Ejecuta La Cadena Del Codigo Y Guarda en Resp
    resp = execute_code_py(str(data['code']))

    #Se Retorna En Formato Json
    return jsonify(resp)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)