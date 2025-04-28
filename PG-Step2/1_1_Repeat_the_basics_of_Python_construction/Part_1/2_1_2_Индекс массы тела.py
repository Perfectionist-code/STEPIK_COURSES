mass, height  = float(input()), float(input())
body_mass_index = mass / height ** 2
if 18.5 <= body_mass_index <= 25:
    print('Оптимальная масса')
elif body_mass_index < 18.5:
    print('Недостаточная масса')
else:
    print('Избыточная масса')
print(body_mass_index)