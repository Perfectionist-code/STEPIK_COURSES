num = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 5 * 25 ** 4 - 2025
res = []
while num:
    num, r = divmod(num, 25)
    res.append(r)
print(res.count(0))