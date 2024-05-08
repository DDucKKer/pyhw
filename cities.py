from pywebio.input import input as pw_input
from pywebio.output import put_success


def check_char(word):
    char_list = ".!@#$%^&*()_+-=~`\\|?/.';:[]{}0123456789№\""
    for char in char_list:
        if char in word:
            word = word.replace(char, '')
    return word


cities_in_last_ten_years = pw_input('Введіть через пробіл міста, в яких ви були за минулі 10 років', required=True)
cities_in_next_ten_years = pw_input('міста, куди він хоче поїхати внаступні 10 років', required=True)
# cities_in_last_ten_years = 'Київ,Одеса Львів ЖитомиР-20 213 -= Ужгород Харків Славутич'
# cities_in_next_ten_years = 'Київ Одеса Львів Житомир-20 Дніпро Вінниця Чернігів'

cities_in_last_ten_years = set(check_char(cities_in_last_ten_years.replace(',', ' ')).title().split())
cities_in_next_ten_years = set(check_char(cities_in_next_ten_years.replace(',', ' ')).title().split())


# print(cities_in_last_ten_years)
# print(cities_in_next_ten_years)
# print('#################################')
common_cities = cities_in_last_ten_years & cities_in_next_ten_years

if common_cities:
    string_common = ', '.join(common_cities)
    put_success(f'Мабуть, дуже сподобалося в цих містах: {string_common}')
else:
    put_success('Ти відкритий до чогось нового')
