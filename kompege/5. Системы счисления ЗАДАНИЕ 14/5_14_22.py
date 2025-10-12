from string import printable

for x in printable[1:12]:
    a = int(f'3364{x}',11) + int(f'{x}7946',12)
    b = int(f'55{x}87', 14)
    if a == b:
        print(x, b)
        break
