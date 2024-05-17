import requests

def view_services(API_KEY,API_URL,Headers):
    #Se Llena La Accion A Realizar
    data = {'key':API_KEY, 'action':'services'}

    #Se Hace La Consulta
    resp = requests.post(API_URL,data=data).json()

    return resp

#data = view_services("7b08dd9f72cc704ffb1d3e74997df7ff","https://smmengineer.com/api/v2",None)
