from string import printable

for p in range(10, 36):
    for x in printable[:p]:
        for y in printable[:p]:
            if int(f'397{x}', p) + int(f'{x}9{x}4', p) == int(f'{y}19{y}', p):
                print(int(f'{x}{x}{y}{y}', p))
