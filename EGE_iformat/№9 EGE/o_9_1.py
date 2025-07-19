with open('o_9_1.txt', 'r') as file:
    cnt = 0
    for l in file:
        l = sorted(map(int, l.split()))
        if l[2] ** 2 > 2 * (l[0] * l[1]):
            cnt += 1
    print(cnt)
