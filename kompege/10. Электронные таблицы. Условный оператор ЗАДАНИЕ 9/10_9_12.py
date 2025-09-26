with open('10_9_12.txt', 'r') as file:
    cnt = 0
    for s in file:
        lst = list(map(int, s.split()))
        if sum(lst) == 360 and lst[0] == lst[2] and lst[1] == lst[3]:
            cnt += 1
print(cnt)
