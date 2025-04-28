d = {tuple(key): value for value, *key in (input().split() for _ in range(int(input())))}
request_lst = [input() for __ in range(int(input()))]
d_1 ={}
for keys, value in d.items():
    d_1 |= d_1.fromkeys(keys, value)
for request in request_lst:
    print(d_1.get(request, 'Такой город в словаре не найден'))



# d = {}
# for _ in range(int(input())):
#     country, *cities = input().split()
#     d.update(dict.fromkeys(cities, country))
# for _ in range(int(input())):
#     print(d[input()])

# d = {s.split()[k]: s.split()[0] for _ in range(int(input())) for s in [input()] for k in range(1, len(s.split()))}
# print(*(d[input()] for _ in range(int(input()))), sep='\n')