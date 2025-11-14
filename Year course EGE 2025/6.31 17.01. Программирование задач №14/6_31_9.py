from string import printable


def f(n: str):
    result = int(f'627{n}j8', 20) + int(f'h45i{n}5hij', 20) + int(f'4idb49j{n}7', 20)
    return result

print(printable[:20][::-1])
for x in printable[:20][::-1]:
    if (r := f(x)) % 19 == 0:
        print(r // 19)
        break
