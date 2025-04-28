# Решение 2
lst = []
lst_res = []
row_cubes = [x ** 3 for x in range(50)]
while len(lst_res) < 5:
    for n in row_cubes:
        for k in row_cubes[row_cubes.index(n):]:
            for m in range(1729, 35000):
                if n + k == m:
                    lst.append(m)
                    if lst.count(m) == 2:
                        lst_res.append(m)
print(*sorted(lst_res))

# Решение 1
# lst = []
# for n in range(1, 100):
#     for k in range(n , 100):
#         for m in range(1729, 35000):
#             if n** 3 + k ** 3 == m:
#                 lst.append(m)
#                 # print('n =', n, 'k =', k, 'm =', m)
# res_lst = sorted(set(filter(lambda x: lst.count(x) >=2, lst)))
# print(*res_lst[:5])

