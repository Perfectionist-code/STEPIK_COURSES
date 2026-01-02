num = 3 * 2187 ** 1801 + 729 ** 2000 - 4 * 243 ** 2100 + 81 ** 2200 - 2 * 27 ** 2400 - 13122

cnt = 0
while num:
    num, r = divmod(num, 27)
    if r > 8:
        cnt += 1
print(cnt)
