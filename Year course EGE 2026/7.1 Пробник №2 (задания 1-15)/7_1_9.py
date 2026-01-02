with open('9.txt') as file:
    cnt = 0
    for i, s in enumerate(file, 1):
        l = tuple(map(int, s.split()))
        l_rep_3 = tuple(x for x in l if l.count(x) == 3)
        l_fr = tuple(x for x in l if l.count(x) == 1)
        if len(set(l_rep_3)) == 1 and len(l_fr) == 4 and sum(l_fr) > sum(l_rep_3):
            print(i, '|', *l)
            cnt = i
print('----' * 5)
print(cnt)
