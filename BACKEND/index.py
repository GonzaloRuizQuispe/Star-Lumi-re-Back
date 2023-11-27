from flask import Flask, request, jsonify
from flask_cors import CORS
from libs.users_db import users
from libs.admin_db import admins

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

    #Se Recolecta El Archivo Json
    data = request.json

    #Si En La Peticion Esta "Codigo" Se Usa La Creación Por Administrador
    if data['codigo']:
        pass

    #Se Retorna En Formato Json
    #return jsonify(resp)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)