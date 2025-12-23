with open('09.txt') as file:
    cnt = 0
    for s in file:
        l = sorted(map(int, s.split()))
        if len(set(l)) == len(l) and sum(l[-2:]) <= sum(l[:-2]):
            cnt += 1
print(cnt)
