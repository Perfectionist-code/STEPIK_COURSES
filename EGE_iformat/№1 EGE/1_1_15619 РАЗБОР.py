# from itertools import permutations
# table = '467 35 257 47 236 15 134'.split()
# graph = 'BA AG AD GE DC CE CF EF'.split()
# print('1 2 3 4 5 6 7')
# for p in permutations('ABCDEFG'):
#     if all(str(p.index(c2)+1) in table[p.index(c1)] for c1, c2 in graph):
#         print(*p)
#         # break

from itertools import permutations
table = '467 35 257 47 236 15 134'.split()
graph = 'BA AG AD GE DC CE CF EF'.split()
print('1 2 3 4 5 6 7')
for p in permutations('ABCDEFG'):
    print(p)
    for c1, c2 in graph:
        print(table)
        print(c1, c2)
        print(str(p.index(c2) + 1), table[p.index(c1)])
        a = str(p.index(c2) + 1) in table[p.index(c1)]
        print(a)
        print('-----' * 3)

    print('#####' * 10)

#     if all(str(p.index(c2)+1) in table[p.index(c1)] for c1, c2 in graph):
#         print(*p)
#         break
