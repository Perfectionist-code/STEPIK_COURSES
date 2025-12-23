from math import prod

with open('03.txt') as file:
    cnt = 0
    for i, s in enumerate(file, 1):
        l = sorted(map(int, s.split()))
        if len(l) == len(set(l)) and (l[0] + l[-1]) ** 2 > prod(l[1:-1]):
            cnt += i
            print(*l)  # Для проверки
print('----' * 10)
print(cnt)
