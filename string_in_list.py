string = "київ,оДеса     Львів.житоМИР,уЖгОрОд.....ХарКІВ       , слАвУтИч".replace('.', ',').replace(' ', ',')
mass = list(filter(None, string.title().split(',')))

print(mass)

for i in mass:
    print(f'Я \u2764 {i}!')
