import requests

headers = {'Accept': 'application/json; version=v2'}
# headers = {'Accept': 'application/json; version=v1'}

response = requests.get('http://127.0.0.1:8000/api/users/', headers=headers)

print(response.json())
