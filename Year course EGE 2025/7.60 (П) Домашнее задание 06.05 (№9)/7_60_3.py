from math import prod

with open('03.txt') as file:
    sum_i = 0
    for i, s in enumerate(file, 1):
        lst = tuple(map(int, s.split()))
        l_rep = tuple(x for x in lst if lst.count(x) > 1)
        if not l_rep:
            l_rep = (0,)
        l_fr = tuple(x for x in lst if lst.count(x) == 1)
        cond_1 = all(not ((lst[j] % 2 == 0) == (lst[j + 1] % 2 == 0)) for j in range(len(lst) - 1))
        if cond_1:
            if 3 * sum(l_fr) >= prod(l_rep):
                print(f'{i}.', *lst)
                sum_i += i
print('---' * 10)
print(sum_i)
