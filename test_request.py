import requests

url = 'http://127.0.0.1:5000/generate'

data = {
    'prompt': 'Cosa pensi del futuro?'
}

response = requests.post(url, json=data)

print(response.json())  # Visualizza la risposta
