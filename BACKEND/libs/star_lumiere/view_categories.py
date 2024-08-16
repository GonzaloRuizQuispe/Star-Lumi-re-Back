import requests

def view_categorys(services):
   
    #Se Hace La Consulta
    resp = services

    data = []
    
    for x in resp:
        if x['category'] not in data:
            data.append(x['category'])
        else:
            pass

    return data