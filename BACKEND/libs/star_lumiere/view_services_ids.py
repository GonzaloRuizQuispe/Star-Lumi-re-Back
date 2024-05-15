import requests

def view_services_ids(tuple_ids,API_KEY,API_URL):
    #Se Llena La Accion A Realizar
        data = {'key':API_KEY, 'action':'services'}

        #Se Hace La Consulta
        resp = requests.post(API_URL,data=data).json()

        data = []

        for x in resp:
            if int(x['service']) in tuple_ids:
                data.append({"id":x['service'],"name":x["name"], "type":x["type"], "rate":x["rate"], "min":x["min"], "max":x["max"],"category":x['category']})
                
        return data


""" juan = [14209, 14208, 14207, 14206, 14205, 14204, 14201]
print(view_services_ids(juan,"7b08dd9f72cc704ffb1d3e74997df7ff","https://smmengineer.com/api/v2")) """
