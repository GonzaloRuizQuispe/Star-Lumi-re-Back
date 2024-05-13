import requests

def view_services(API_KEY,API_URL,Headers):
    #Se Llena La Accion A Realizar
    data = {'key':API_KEY, 'action':'services'}

    #Se Hace La Consulta
    resp = requests.post(API_URL,data=data).json()

    return resp