with open('9var1.txt') as file:
    cnt = 0
    for s in file:
        l = sorted(map(int, s.split()), reverse=True)
        if l[0] < sum(l[1:]) and len(l) == len(set(l)):
            cnt += 1
            print(*l)
print('----' * 5)
print(cnt)
