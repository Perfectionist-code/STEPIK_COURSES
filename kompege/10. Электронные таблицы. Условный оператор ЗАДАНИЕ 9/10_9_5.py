with open('10_9_5.txt', 'r') as file:
    cnt = 0
    for s in file:
        lst = sorted(map(int, s.split()))
        if (lst[0] + lst[-1]) / 2 == lst[1]:
            cnt += 1
print(cnt)