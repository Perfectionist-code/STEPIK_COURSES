with open('17_2_1733751344.txt') as file:
    a = tuple(int(x) for x in file)
min_pos_2025 = min(x for x in a if x > 0 and x % 2025 == 0)
# print(min_pos_2025)
res = []
for l in zip(a, a[1:], a[2:], a[3:]):
    if l[0] > 0 and l[-1] > 0 and abs(l[2] - l[1]) <= min_pos_2025:
        res.append(sum(l))
        print(*l)
print('----' * 5)
print(len(res), min(res))
