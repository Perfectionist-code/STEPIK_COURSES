from string import printable

for x in printable[:17]:
    a = int(f'9759{x}',17) + int(f'3{x}108',17)
    if not a % 11:
        print(x, a//11)
        break
