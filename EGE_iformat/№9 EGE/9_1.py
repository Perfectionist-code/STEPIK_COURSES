with open('9_1.txt', 'r') as file:
    cnt = 0
    for l in file:
        l = sorted(map(int, l.split()))
        if (l[0] + l[-1]) ** 2 > sum([x ** 2 for x in l[1:-1]]):
            cnt += 1
    print(cnt)
