def get_r(n: int):
    if not n % 3:
        r = n // 3
    else:
        r = n - 1
    if not r % 5:
        r //= 5
    else:
        r -= 1
    if not r % 11:
        r //= 11
    else:
        r -= 1
    return r

cnt = 0
for num in range(2, 10000000):
    if get_r(num) == 8:
        print(num)
        cnt += 1
print(cnt)
