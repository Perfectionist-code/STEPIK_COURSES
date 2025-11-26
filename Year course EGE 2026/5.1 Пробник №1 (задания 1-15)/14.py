res = []
for x in range(1, 1951):
    num = 72070 + 7400 - x
    cnt = 0
    while num:
        num, r = divmod(num, 9)
        if r == 0:
            cnt += 1
    res.append(cnt)
print(max(res))
