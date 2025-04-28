tup = tuple(int(x) for x in input().split())
res_set = set()
len_set = len(res_set)
for num in tup:
    res_set.add(num)
    print(('NO', 'YES')[len_set == len(res_set)])
    len_set = len(res_set)