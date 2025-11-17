cnt = 0
num = 16807 ** 35 + 2401 ** 2 * 343 ** 9 - 49 ** 52 + 7 ** 3 - 2005
while num:
    num, r = divmod(num, 49)
    if r > 9:
        cnt += 1
print(cnt)
