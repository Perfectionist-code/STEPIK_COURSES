def get_divisors(num: int):
    divisors = set()
    for d in range(2, int(num ** .5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
        if len(divisors) > 3:
            return False
    return divisors if len(divisors) == 3 else False


for n in range(106_732_567, 152_673_837):
    if dv:=get_divisors(n):
        print(n, max(dv))
