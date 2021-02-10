import requests

test = { 
        "items": {
            "price": 50,
            "name": "Apples",
            "description": "Краснодарские",
            "deleted": False
        }
    }

url = 'http://127.0.0.1:8000/api/items/4'

response = requests.put(url, data=dict(test))
print(response.json())