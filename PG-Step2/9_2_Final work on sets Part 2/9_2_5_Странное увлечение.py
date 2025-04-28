set_1 = {int(x) for x in input().split()}
set_2 = {int(y) for y in input().split()}
if set_1 & set_2 == set():
    print('BAD DAY')
else:
    print(*sorted(set_1 & set_2, reverse = True))


# set1 = {int(i) for i in input().split()}
# set2 = {int(i) for i in input().split()}
#
# if set1.isdisjoint(set2):
#     print('BAD DAY')
# else:
#     print(*sorted(set1 & set2, reverse=True))