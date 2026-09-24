import requests
respuesta = requests.get("https://api.exchangerate-api.com/v4/latest/EUR")
datos = respuesta.json()
print(datos["rates"]["USD"])