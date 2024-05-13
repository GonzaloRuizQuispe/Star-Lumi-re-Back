import requests

def view_categorys(API_KEY,API_URL,Headers):
    #Se Llena La Accion A Realizar
    data = {'key':API_KEY, 'action':'services'}

    #Se Hace La Consulta
    resp = requests.post(API_URL,data=data).json()

    data = []
    
    for x in resp:
        if x['category'] not in data:
            data.append(x['category'])
        else:
            pass

    return data