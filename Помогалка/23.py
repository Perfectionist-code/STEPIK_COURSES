# def f(curr, cnt):
#     if cnt > 5: return 0
#     if cnt == 5: return 1
#     return f(curr + 4, cnt + 1) + f(curr * 2, cnt + 1)
#
# print(f(2,0))

from itertools import product

cnt = 0

res = []
for per in product(('+4', '*2'), repeat=5):
    a = 2
    for p in per:
        if p == '+4':
            a += 4
        if p == '*2':
            a *= 2
    res.append(a)
print(len(set(res)), set(res))