tup = tuple(input().split() for _ in range(int(input())))
d_1 = dict(tup)
d_1 |= {value: key for key, value in tup}
request = input()
print(d_1.get(request, 'Запрос в словаре не найден'))

