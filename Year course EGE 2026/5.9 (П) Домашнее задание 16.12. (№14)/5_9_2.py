num = 5 * 343 ** 8 + 4 * 49 ** 12 + 7 ** 14 - 98

res = []
while num:
    num, r = divmod(num, 7)
    res.append(str(r))
n = res[::-1]
print(max(n, key=lambda x: n.count(x)))
