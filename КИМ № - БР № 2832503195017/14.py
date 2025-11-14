from reprlib import recursive_repr
from string import printable

def f(x:str):
    return int(f'11h{x}05', 18) + int(f'3f{x}54{x}8', 18) + int(f'g{x}{x}{x}9', 18)

for X in printable[:18]:
    num = f(X)
    if num % 14 == 0:
        print(num // 14)
        break