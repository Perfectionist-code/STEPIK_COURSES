with open('o_9_2.txt', 'r') as file:
    cnt = 0
    for l in file:
        l = sorted(map(int, l.split()))
        if l[0] + l[3] <= l[1] + l[2]:
            cnt += 1
    print(cnt)
