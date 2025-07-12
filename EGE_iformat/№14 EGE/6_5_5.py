from functools import reduce
from string import digits
# res = []
res = 0
for x in digits:
    a = int('84' + x + '9999', 14)
    b = int('1' + x + '765', 16)
    if not ((d:=(a + b)) % 6):
        res += d
        # res.append((x, d // 14))
# print(*res, sep='\n')
print(res)
res = reduce(lambda a,b: int(a) * int(b), filter(lambda x: x != '0', str(res)))
print(res)
