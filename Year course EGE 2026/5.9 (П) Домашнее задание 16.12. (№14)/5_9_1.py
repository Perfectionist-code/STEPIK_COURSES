num = 11 * 15 ** 65 + 18 * 15 ** 38 - 14 * 15 ** 17 + 19 * 15 ** 11 + 18338

res = set()
while num:
    num, r = divmod(num, 15)
    res.add(r)
print(len(res))
