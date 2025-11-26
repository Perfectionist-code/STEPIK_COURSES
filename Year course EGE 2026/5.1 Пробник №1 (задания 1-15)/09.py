from statistics import mean

with open('9_1729261748.txt') as file:
    cnt = 0
    for s in file:
        l = sorted(map(int, s.split()))
        if len(l) == len(set(l)) and mean((l[0], l[-1])) <= mean(l[1:-1]):
            cnt += 1
            print(*l)
print('----' * 5)
print(cnt)
