num = 9 ** 7 + 3 ** 21 - 8
res = []
while num:
    num, r = divmod(num, 3)
    res.append(r)
print(sum(res))