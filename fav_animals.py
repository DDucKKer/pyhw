from pywebio.input import input as pw_input
from pywebio.input import NUMBER, PASSWORD, TEXT, DATETIME, COLOR
from pywebio.output import put_success, put_warning, put_code, popup, put_markdown, toast


def delchar(word):
    charlist = ".,!@#$%^&*()_+=~`\\|?/.,\';:[]{}0123456789№\""
    for char in charlist:
        if char in word:
            word = word.replace(char, '')
    return word.title()


cat_emodji = '\U0001F431'
dog_emodji = '\U0001F436'
hamster_emodji = '\U0001F439'
fish_emodji = '\U0001F41F'
turtle_emodji = '\U0001F422'

fav_animal = delchar(pw_input('Enter the name of your favorite animal', type=TEXT, required=True))
pet_name = delchar(pw_input('Enter your pet\'s nickname', type=TEXT, required=True))
pet_can_swim = ''
can_swim = False

if pet_name in ('fish', 'turtle'):
    can_swim = True

if can_swim is False:
    pet_can_swim = pw_input('Can your pet swim? (yes/no)', type=TEXT, required=True, datalist=['yes', 'no'])

    if pet_can_swim == 'yes':
        can_swim = True

if can_swim is True:
    put_success('We need to buy an aquarium')

if fav_animal == 'Cat':
    put_success(f'{fav_animal}s catch mice. How about {pet_name}? {cat_emodji}')

elif fav_animal == 'Dog':
    put_success(f'I am afraid of barking dogs, including {pet_name}. {dog_emodji}')

elif fav_animal == 'Hamster':
    put_success(f'Hamsters are small. {hamster_emodji}')

elif fav_animal == 'Fish':
    put_success(f'Do\'nt fry the fish. {fish_emodji}')

elif fav_animal == 'Turtle':
    put_success(f'{pet_name} has a strong shell. {turtle_emodji}')

else:
    put_success(f'I don\'t know the type of this animal({fav_animal}).')
