d = {key.lower(): value for key, value in (input().split(': ') for _ in range(int(input())))}
request_lst = [input().lower() for _ in range(int(input()))]
for request in request_lst:
    print(d.get(request, 'Не найдено'))

# mydict = {}
#
# for _ in range(int(input())):
#     key, value = input().split(': ')
#     mydict[key.lower()] = value
#
# for _ in range(int(input())):
#     print(mydict.get(input().lower(), 'Не найдено'))


# d = {k.lower(): v for _ in range(int(input())) for k, v in [input().split(': ', 1)]}
# print(*(d.get(input().lower(), 'Не найдено') for _ in range(int(input()))), sep='\n')