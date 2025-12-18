from string import printable


def num_to_10(num: str, cs: int) -> int:
    return sum(printable[:cs].index(x) * cs ** i for i, x in enumerate(num[::-1]))


for x in printable[:37][::-1]:
    a = num_to_10(f'c59{x}ba98f', 37)
    b = num_to_10(f'e3{x}5da9c6', 37)
    if not a * b % 36:
        print(num_to_10(f'2{x}1', 37), x)
        break
