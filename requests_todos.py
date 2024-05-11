import requests

url = 'https://dummyjson.com/todos'
params = {
    'limit': 150,
}
response = requests.get(url=url, params=params)
todos = response.json()['todos']

print('UNCOMPLETED tasks: ')
for todo in todos:
    if not todo["completed"]:
        print(todo['todo'])
