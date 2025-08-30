from decimal import *
getcontext().prec = 1

n = int(input())
res = []
for _ in range(n):
    name = input()
    summ = 0
    for __ in range(4):
        summ += int(input())
    num = Decimal(summ / 4)
    res.append(f'{name} - {(num.quantize(Decimal('1'), ROUND_HALF_UP))}')

print(*res, sep='\n')

