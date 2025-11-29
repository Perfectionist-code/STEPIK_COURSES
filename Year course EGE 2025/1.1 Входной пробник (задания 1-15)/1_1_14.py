from string import printable

for x in printable[:23]:
    num = int(f'2{x}{x}341011', 23) + int(f'220{x}4', 23) + int(f'110{x}6', 23)
    if not num % 22:
        print(num // 22)
        break
