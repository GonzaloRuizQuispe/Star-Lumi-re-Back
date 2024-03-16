""" import hashlib
import hmac
import time
import json
import requests

ts = int(round(time.time()*1000))
method = 'account'
req = json.dumps({
    'ts': ts,
})
print(req)

clave = b'PoolLive45427752'
H = hmac.new(clave, digestmod=hashlib.sha256)
method = str(method)
req = str(req)
H.update(method.encode('utf-8') + req.encode('utf-8'))
sign = H.hexdigest()
print(sign)

headers = {
    'Content-Type': 'application/json',
    'API-ID': 'f26c52a9-858e-4375-81a7-649b969c16aa',
    'API-SIGN': sign
}

request = requests.post('https://payeer.com/api/trade/' + method, data=req, headers=headers)

response_body = request.text
print(response_body) """


