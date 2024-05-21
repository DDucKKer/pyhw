def check_age(age: int) -> str:
    if age <= 0:
        return "Передано не валідне значення віку!"
    elif age <= 18:
        return "Ти дитина!"
    elif age <= 65:
        return "Потрібно працювати!"
    else:
        return "Щасливої пенсії!"


# age = int(input("Введіть свій вік: "))
# print(check_age(age))
