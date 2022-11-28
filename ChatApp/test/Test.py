# import requests
#
# api_url = "https://jsonplaceholder.typicode.com/todos/1"
# response = requests.get(api_url)
# json = response.json()
# print(json)
# print(response.status_code)
#
# print(response.headers["Content-Type"])

# import requests
# api_url = "https://jsonplaceholder.typicode.com/todos"
# todo = {"userId": 1, "title": "Buy milk", "completed": False}
# response = requests.post(api_url, json=todo)
# response.json()
# #{'userId': 1, 'title': 'Buy milk', 'completed': False, 'id': 201}
#
# print(response.status_code)


# import requests
# import json
#
# api_url = "https://jsonplaceholder.typicode.com/todos"
# todo = {"userId": 1, "title": "Buy milk", "completed": False}
# headers =  {"Content-Type":"application/json"}
# response = requests.post(api_url, data=json.dumps(todo), headers=headers)
# print(response.json())
# #{'userId': 1, 'title': 'Buy milk', 'completed': False, 'id': 201}
#
# print(response.status_code)
# #201

# import requests
# api_url = "https://jsonplaceholder.typicode.com/todos/10"
# response = requests.get(api_url)
# response.json()
#
#
# todo = {"userId": 1, "title": "Wash car", "completed": True}
# response = requests.put(api_url, json=todo)
# print(response.json())
#
#
# print(response.status_code)

# import requests
# api_url = "https://jsonplaceholder.typicode.com/todos/10"
# todo = {"title": "Mow lawn"}
# response = requests.patch(api_url, json=todo)
# print(response.json())
#
#
# print(response.status_code)


# import requests
# api_url = "https://jsonplaceholder.typicode.com/todos/10"
# response = requests.delete(api_url)
# print(response.json())
#
#
# print(response.status_code)

from flask import Flask, request, jsonify

app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

def _find_next_id():
    return max(country["id"] for country in countries) + 1

@app.get("/countries")
def get_countries():
    return jsonify(countries)

@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415
