import re
from gettext import translation

hasht = "#" * 80
print(hasht)

lang = input('Choose the language(en, ru, uk, de, fr): ')
translator = translation('this_project', 'locale', [lang], fallback=True)
_ = translator.gettext

name = input(_('Enter your name: ')).capitalize()
surname = input(_('Enter your surname: ')).capitalize()

name = re.sub("[^A-Za-z]", "", name)
surname = re.sub("[^A-Za-z]", "", surname)


if (name.find('ван') is True) or (surname.find('вич') is True):
    print(_("Your name will be changed"))
    name = name.replace('ван', 'ванка')
    surname = surname.replace('вич', '')

print(_("Hello"), name, surname)

print(hasht)
