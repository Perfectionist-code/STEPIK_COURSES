from math import prod

with open('05.txt') as file:
    sum_i = 0
    for i, s in enumerate(file, 1):
        lst = sorted(map(int, s.split()))
        if len(lst) == len(set(lst)) and (lst[0] + lst[-1]) ** 2 > prod(lst[1:-1]):
            print(f'{i}.', *lst)
            sum_i += i
print('------' * 5)
print(sum_i)
