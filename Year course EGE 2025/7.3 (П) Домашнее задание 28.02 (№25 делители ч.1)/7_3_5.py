# def get_d(num: int):
#     divisors = set()
#     for d in range(2, int(num ** .5) + 1):
#         if not num % d:
#             divisors.add(d)
#             divisors.add(num // d)
#     if len(divisors) >= 12:
#         return sorted(divisors)
#     return sorted(divisors) if len(divisors) >=6 else False

def get_divisors(num: int):
    divisors = set()
    for d in range(2, int(num ** .5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return sorted(divisors)


cnt = 0
for n in range(300_000_001, 400_000_000):
    if len(dv := get_divisors(n)) >=6:
        print(dv[-6], dv.__len__())
        cnt +=1
    if cnt == 5:
        break
