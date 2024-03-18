import requests

url ="https://payeer.com/merchant/"

shop = "12345"
order_id = "1"
amount = "100"
curr = "USD"
desc = "Pepe"
sign = "9F86D081884C7D659A2FEAA0C55AD015A3BF4F1B2B0B822CD15D6C15B0F00A08"
key = "Pool!Live45427752"

data = {
    'm_shop':shop,
    'm_orderid':order_id,
    'm_amount':amount,
    'm_curr':curr,
    'm_desc':desc,
    'm_sign':sign,
    'form[ps]':2609,
    'form[curr[psId]]':'USD',
    'm_params':2,
    'm_cipher_method':'AES-256-CBC-IV',
    'm_key':key,
}

resp = requests.post(url=url,data=data)

print(resp.url)