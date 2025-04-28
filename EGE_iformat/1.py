# from itertools import permutations
# table = '24 146 45 12356 34 24'.split()
# graph = 'DC DE DB CB EB BA BG AG'.split()
# print('1 2 3 4 5 6')
# for p in permutations('ABCDEG'):
#     if all(str(p.index(c2)+1) in table[p.index(c1)] for c1, c2 in graph):
#         print(*p)
#         break

from itertools import permutations

table = '24 146 45 12356 34 24'.split()
graph = 'DC DE DB CB EB BA BG AG'.split()
print('1 2 3 4 5 6')
for p in permutations('ABCDEG'):
    print(p)
    for c1, c2 in graph:
        print(c1, c2)
        print(str(p.index(c2) + 1), table[p.index(c1)])
        a = str(p.index(c2) + 1) in table[p.index(c1)]
        print(a)
        print('-----' * 3)

    print('#####' * 10)

    # if all(str(p.index(c2)+1) in table[p.index(c1)] for c1, c2 in graph):
    #     print(*p)
    #     break
