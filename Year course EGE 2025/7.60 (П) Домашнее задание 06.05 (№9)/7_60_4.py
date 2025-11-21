from itertools import permutations


def cond2(l: list) -> bool:
    for a, b, c, d in permutations(l):
        if all(((a + b) % 2, (c + d) % 2)):
            return True
    return False


with open('04.txt') as file:
    sum_i = 0
    for i, s in enumerate(file, 1):
        lst = sorted(map(int, s.split()))
        l_rep_3 = tuple(x for x in lst if lst.count(x) == 3)
        l_rep_2 = tuple(x for x in lst if lst.count(x) == 2)
        if set(l_rep_3).__len__() == 1 and set(l_rep_2).__len__() == 2 and cond2(lst[:4]):
            print(f'{i}.', *lst)
            sum_i += sum(lst)
print('---' * 10)
print(sum_i)
