with open('08.txt') as file:
    cnt = 0
    for s in file:
        l = sorted(map(int, s.split()))
        l_rep = tuple(x for x in l if l.count(x) > 1)
        l_fr = sorted(x for x in l if l.count(x) == 1)
        if max(l) in l_rep and len(set(l_rep)) == 1 and len(l_rep) in (3, 4) and l_fr[0] + l_fr[-1] <= sum(l_fr[1:-1]):
            cnt += 1
            print(*l)  # Для проверки
print('----' * 10)
print(cnt)
