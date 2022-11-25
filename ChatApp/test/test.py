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
