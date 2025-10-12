from string import printable

for x in printable[:15]:
    a = int(f'123{x}5', 15)
    for y in printable[:17]:
        b = int(f'67{y}9', 17)
        if (a + b) % 131 == 0:
            print(int(x, 15), int(y, 17), (a + b) // 131)
