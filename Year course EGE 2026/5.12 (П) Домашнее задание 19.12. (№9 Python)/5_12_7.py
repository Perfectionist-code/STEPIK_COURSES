with open('07.txt') as file:
    cnt = 0
    for i, s in enumerate(file, 1):
        l = sorted(map(int, s.split()))
        l_rep = tuple(x for x in l if l.count(x) > 1)
        l_fr = tuple(x for x in l if l.count(x) == 1)
        if l_rep and l_fr and sum(l_rep) ** 2 > sum(l_fr) ** 2 and sum(l) % 2:
            cnt = i
            print(*l)  # Для проверки
print('----' * 10)
print(cnt)
