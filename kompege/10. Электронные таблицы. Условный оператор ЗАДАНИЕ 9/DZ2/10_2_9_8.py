from math import prod

with open('08_9_4636.txt') as file:
    cnt = 0
    for s in file:
        lst = sorted(map(int, s.split()))
        if lst[-1] - lst[0] >= 50 and prod(lst[1:-1]) <= 1000:
            cnt += 1
            print(*lst)
print('----' * 5)
print(cnt)
