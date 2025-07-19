with open('9_2.txt', 'r') as file:
    cnt = 0
    for l in file:
        l = list(map(int, l.split()))
        if (l[0] + l[1]) / 2 == l[2]:
            cnt += 1
    print(cnt)
