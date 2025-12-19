with open('09.txt') as file:
    sm = 0
    for s in file:
        l = list(map(int, s.split()))
        if all(l[i] < l[i + 1] for i in range(len(l) - 1)) and sum(x % 2 == 0 for x in l) == 3:
            sm = sum(l)
            print(*l)  # Для проверки
print('----' * 10)
print(sm)
