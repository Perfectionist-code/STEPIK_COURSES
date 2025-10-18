def find_divisors(num: int):
    res = []
    for d in range(2, num // 2 + 1):
        if not num % d:
            res.append(d)
    return (len(res), sum(res)) if sum(res) > 460000 else False

for n in range(135790,163229):
    if dv:=find_divisors(n):
        print(*dv)

# from sympy import divisors
#
# for n in range(135790,163229):
#     if (sm:=sum(dv:=divisors(n)[1:-1])) > 460000:
#         print(len(dv), sm)