with open('01.txt') as file:
    cnt = 0
    for i, s in enumerate(file, 1):
        lst = list(map(int, s.split()))
        lst_sorted = sorted(lst)
        l_rep = tuple(x for x in set(lst) if lst.count(x) > 1)
        if lst == lst_sorted and any(sum(int(ch) for ch in str(x)) % 2 == 0 for x in l_rep):
            print(f'{i}.', *lst_sorted)
            cnt = i
print(cnt)
