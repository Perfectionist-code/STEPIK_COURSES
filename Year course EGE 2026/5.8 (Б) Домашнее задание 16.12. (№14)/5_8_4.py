num = 2 * 2401 ** 525 + 3 * 343 ** 524 - 4 * 49 ** 523 + 5 * 49 ** 522 - 6 * 7 ** 521 - 35
cnt = 0
while num:
    num, r = divmod(num, 49)
    if r <= 9:
        cnt += 1
print(cnt)