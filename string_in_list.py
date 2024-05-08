string = "київ,оДеса     Львів.житоМИР,уЖгОрОд.....ХарКІВ       , слАвУтИч"
string = string.replace('.', ',').replace(' ', ',').title().split(',')
citiesList = list(filter(None, string))

print(citiesList)

for i in citiesList:
    print(f'Я \u2764 {i}!')
