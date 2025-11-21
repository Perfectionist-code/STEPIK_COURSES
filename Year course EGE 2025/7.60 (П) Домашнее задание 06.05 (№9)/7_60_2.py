with open('02.txt') as file:
    cnt = 0
    for i, s in enumerate(file, 1):
        lst = sorted(map(int, s.split()))
        l_even = tuple(x for x in lst if not x % 2)
        l_odd = tuple(x for x in lst if x % 2)
        if len(l_odd) == len(l_even) and lst[0] + lst[-1] == lst[1] + lst[-2] == lst[2] + lst[-3]:
            print(f'{i}.', *lst)
            cnt = i
print('---' * 10)
print(cnt)
