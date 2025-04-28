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
    for line in graph:
        l1, l2 = line
        print(l1, l2)
        print(str(p.index(l2) + 1), table[p.index(l1)])
        a = str(p.index(l2) + 1) in table[p.index(l1)]
        print(a)
        print('-----' * 3)

    print()
    print('#####' * 10)
    print()

    # if all(str(p.index(c2)+1) in table[p.index(c1)] for c1, c2 in graph):
    #     print(*p)
    #     break
