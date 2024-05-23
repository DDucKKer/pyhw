iso_country = 'UA'

with open('airport_codes.csv', mode='r', encoding='utf-8') as file:
    for line in file.readlines():
        data = line.split(';')
        if data[5] == iso_country:
            print(data[2])

