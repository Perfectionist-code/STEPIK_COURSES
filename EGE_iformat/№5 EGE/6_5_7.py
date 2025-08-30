from string import digits

res = 0
for x in digits:
    for y in digits:
        a = int('7' + y + x + '777', 13)
        b = int('6' + x + '66' + y + '6', 17)
        if not ((d := (a + b)) % 16):
            # print(x, y)
            res += d
print(res)
