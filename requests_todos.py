import requests
# from pprint import pprint

url = 'https://dummyjson.com/todos'
params = {
    'limit': 150,
}
response = requests.get(url=url, params=params)
# pprint(response.json())
todos = response.json()['todos']

print('UNCOMPLETED tasks: ')
for todo in todos:
    if todo["completed"] is False:
        print(todo['todo'])

