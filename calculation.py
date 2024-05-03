from decimal import Decimal


OSTRICH_EGG = 118
RABBIT = 197
SEA_BASS = 123
SWEET_RED_PEPPER = 26
PARSLEY = 45
BANANAS = 87
WAFFLES = 425
BREAD = 246
PISTACHIOS = 555
KEFIR = 51

KKAL_COST = 0.32541
total_calorie = 0

hasht = "#" * 80
print(hasht)

ostrich_egg_count = int(input('Введіть кількість страусиного яйця в грамах: '))
order_cal = Decimal(OSTRICH_EGG/100 * ostrich_egg_count).quantize((Decimal('0.00')))
total_calorie += order_cal
print(f'Калорійність замовленої позиції - {order_cal}')
print(f'Загальна калорійність всього замовлення - {total_calorie}')
print(hasht)

rabbit_count = int(input('Введіть кількість кролика в грамах: '))
order_cal = Decimal(str(RABBIT/100 * rabbit_count)).quantize((Decimal('0.00')))
total_calorie += order_cal
print(f'Калорійність замовленої позиції - {order_cal}')
print(f'Загальна калорійність всього замовлення - {total_calorie}')
print(hasht)

sea_bass_count = int(input('Введіть кількість морського окуня в грамах: '))
order_cal = Decimal(str(SEA_BASS/100 * sea_bass_count)).quantize((Decimal('0.00')))
total_calorie += order_cal
print(f'Калорійність замовленої позиції - {order_cal}')
print(f'Загальна калорійність всього замовлення - {total_calorie}')
print(hasht)

sweet_red_pepper_count = int(input('Введіть кількість солодкого червоного перця в грамах: '))
order_cal = Decimal(str(SWEET_RED_PEPPER/100 * sweet_red_pepper_count)).quantize((Decimal('0.00')))
total_calorie += order_cal
print(f'Калорійність замовленої позиції - {order_cal}')
print(f'Загальна калорійність всього замовлення - {total_calorie}')
print(hasht)

parsley_count = int(input('Введіть кількість петрушки в грамах: '))
order_cal = Decimal(str(PARSLEY/100 * parsley_count)).quantize((Decimal('0.00')))
total_calorie += order_cal
print(f'Калорійність замовленої позиції - {order_cal}')
print(f'Загальна калорійність всього замовлення - {total_calorie}')
print(hasht)

bananas_count = int(input('Введіть кількість бананів в грамах: '))
order_cal = Decimal(str(BANANAS/100 * bananas_count)).quantize((Decimal('0.00')))
total_calorie += order_cal
print(f'Калорійність замовленої позиції - {order_cal}')
print(f'Загальна калорійність всього замовлення - {total_calorie}')
print(hasht)

waffles_count = int(input('Введіть кількість вафлей в грамах: '))
order_cal = Decimal(str(WAFFLES/100 * waffles_count)).quantize((Decimal('0.00')))
total_calorie += order_cal
print(f'Калорійність замовленої позиції - {order_cal}')
print(f'Загальна калорійність всього замовлення - {total_calorie}')
print(hasht)

bread_count = int(input('Введіть кількість хлібу в грамах: '))
order_cal = Decimal(str(BREAD/100 * bread_count)).quantize((Decimal('0.00')))
total_calorie += order_cal
print(f'Калорійність замовленої позиції - {order_cal}')
print(f'Загальна калорійність всього замовлення - {total_calorie}')
print(hasht)

pistachios_count = int(input('Введіть кількість фісташек в грамах: '))
order_cal = Decimal(str(PISTACHIOS/100 * pistachios_count)).quantize((Decimal('0.00')))
total_calorie += order_cal
print(f'Калорійність замовленої позиції - {order_cal}')
print(f'Загальна калорійність всього замовлення - {total_calorie}')
print(hasht)

kefir_count = int(input('Введіть кількість кефіру 2,5% в грамах: '))
order_cal = Decimal(str(KEFIR/100 * kefir_count)).quantize((Decimal('0.00')))
total_calorie += order_cal
print(f'Калорійність замовленої позиції - {order_cal}')
print(f'Загальна калорійність всього замовлення - {total_calorie}')
print(hasht)


if total_calorie < 1000:
    print('Bи, мабуть залишитеся голодним!')
elif 1000 < total_calorie < 1500:
    print('Це саме ваш варіант вечері!')
else:
    print('Bи стільки не зїсте, і це все гроші в смітник!')

print(hasht)
total_cost = Decimal(str(int(total_calorie) * KKAL_COST)).quantize((Decimal('0.00')))

print(f'Загальна ціна - {total_cost}')
