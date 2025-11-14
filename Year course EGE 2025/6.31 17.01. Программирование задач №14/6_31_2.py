num = 7 * 512 ** 3200 + 6 * 256 ** 3100 - 5 * 64 ** 3000 - 4 * 8 ** 2900 - 1542
res = []
cnt = 0
while num:
    num, r = divmod(num, 64)
    res.append(str(r))
    if r == 0:
        cnt += 1
num = ''.join(res[::-1])
print(cnt)
print(num)
print(num.count('0'))
