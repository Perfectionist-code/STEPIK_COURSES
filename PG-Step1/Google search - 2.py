lst = [input().strip() for _ in range(int(input()))]
search_query_lst = [input().strip() for _ in range(int(input()))]
res = []

for search_query in search_query_lst:
    for _str in lst:
        if search_query.lower() in _str.lower() and _str not in res:
            res.append(_str)
for search_query in search_query_lst:
    for i, _str in enumerate(res):
        if search_query.lower() not in _str.lower():
            res[i] = ''
while '' in res:
    res.remove('')
print(*res, sep = '\n')
