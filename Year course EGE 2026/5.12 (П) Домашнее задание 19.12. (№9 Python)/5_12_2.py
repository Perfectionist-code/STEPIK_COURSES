with open('02.txt') as file:
    cnt = 0
    for i, s in enumerate(file, 1):
        l = sorted(map(int, s.split()))
        l_rep_3 = tuple(x for x in l if l.count(x) == 3)
        l_fr = tuple(x for x in l if l.count(x) == 1)
        if len(set(l_rep_3)) == 1 and len(l_fr) == 4 and sum(x % 2 == 0 for x in l) > 3:
            cnt = i
            print(*l)  # Для проверки
print('----' * 10)
print(cnt)
