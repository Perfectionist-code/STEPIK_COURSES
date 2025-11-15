from string import printable


def f(x: str, y: str, p: int) -> bool:
    return int(f'89{x}0', p) + int(f'{x}6{x}4', p) == int(f'1{y}{y}14', p)


for p in range(10, 36):
    for x in printable[:p]:
        for y in printable[:p]:
            if f(x, y, p):
                print(int(f'{y}{x}{y}{x}', p))
