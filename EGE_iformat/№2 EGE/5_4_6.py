# res = 0
# for i in range(1000, 10000):
#     num = str(i)
#     if all((num[0] == num[1], num[2] == num[3])):
#         res += 1
# print(res//2)

from itertools import product
res = 0
for per in product('0123456789', repeat=4):

    if all((per[0] == per[1], per[2] == per[3])):
        res += 1
print(res)
