import requests
# from pprint import pprint

url = 'http://api.open-notify.org/astros.json'
response = requests.get(url)
# pprint(response.json())
people = response.json()['people']
cosmo_people_list = []

for person in people:
    cosmo_people_list.append(person['name'])

print(cosmo_people_list)
