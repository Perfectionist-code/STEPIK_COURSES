num = 27 ** 4 - 9 ** 5 + 3 ** 8 - 25
cnt = 0
while num:
    num, r = divmod(num, 3)
    if r == 2:
        cnt += 1
print(cnt)
