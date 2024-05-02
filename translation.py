from gettext import translation

hasht = "#" * 80
print(hasht)

lang = input('Choose the language(en, ru, uk, de, fr): ')
translator = translation('this_project', 'locale', [lang], fallback=True)
_ = translator.gettext

name = input(_('Enter your name: '))
surname = input(_('Enter your surname: '))


def strng(word):
    charlist = " .,!@#$%^&*()_+-=~`\\|?/.,';:[]{}0123456789№\""
    for char in charlist:
        if char in word:
            word = word.replace(char, '')
    return word


name = strng(name)
surname = strng(surname)

if (name.find('ван') != -1) or (surname.find('вич') != -1):
    print(_("Your name will be changed"))
    name = name.replace('ван', 'ванка')
    surname = surname.replace('вич', '')


print(_("Hello"), name.capitalize(), surname.capitalize())

print(hasht)
