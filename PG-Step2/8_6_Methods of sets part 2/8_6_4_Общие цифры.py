lst = [input() for _ in range(int(input()))]
res_set = set(lst[0])
for i in range(1, len(lst)):
    res_set.intersection_update(lst[i])
print(*sorted(res_set))