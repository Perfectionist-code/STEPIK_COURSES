def is_even_number(num: int) -> bool:
    return not x % 2


for x in (55, 21, 30, 42):
    if (is_even_number(x) or not x % 3) and not x % 7:
        print(x)
