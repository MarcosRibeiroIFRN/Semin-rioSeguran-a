import requests

host = "http://localhost:8081/"
metodos = [

       "OPTIONS",
    "GET",
    "POST",
    "PUT",
    "DELETE",
    "TRACE",
    "CONNECT"
    
]

for metodo in metodos:
    resposta = requests.request(metodo, host)
    print(f"{metodo} -> {resposta.status_code} ({resposta.reason})")
