with open('10_9_10.txt', 'r') as file:
    cnt1 = 0
    cnt2 = 0
    for s in file:
        lst = list(map(int, s.split()))
        if sum(lst) == 180:
            cnt1 += 1
            if len(set(lst)) < 3:
                cnt2 += 1

print(cnt1, cnt2, int(cnt2/cnt1*100))
