with open('09_1733748431.txt') as file:
    cnt = 0
    for s in file:
        l = sorted(map(int, s.split()))
        l_rep = tuple(x for x in l if l.count(x) > 1)
        l_even = tuple(x for x in l if x % 2 == 0)
        l_odd = tuple(x for x in l if x % 2 != 0)
        cond1 = len(l_rep) == 3 and len(set(l)) == 4
        cond2 = len(l_even) > len(l_odd)
        cond3 = sum(l[-2:]) / sum(l[:-2]) > 2
        if cond1 + cond2 + cond3 >= 2:
            cnt += 1
print('----' * 5)
print(cnt)
