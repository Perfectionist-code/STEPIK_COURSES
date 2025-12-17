num = 49 ** 12 - 7 ** 10 + 7 ** 8 - 49
cnt = 0
while num:
    num, r = divmod(num, 7)
    if r == 6:
        cnt += 1
print(cnt)
