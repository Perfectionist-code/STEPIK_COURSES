with open('06.txt') as file:
    sm = 0
    for i, s in enumerate(file, 1):
        l = sorted(map(int, s.split()))
        if (l[0] + l[-1]) ** 2 > sum(x ** 3 for x in l[1:-1]) and l[0] + l[-1] != l[1] + l[2]:
            sm += i
            print(*l)  # Для проверки
print('----' * 10)
print(sm)
