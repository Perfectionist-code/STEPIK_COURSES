with open('10_9_9.txt','r') as file:
    cnt = 0
    for s in file:
        lst = list(map(int, s. split()))
        if sum(lst) == 180:
            print(*lst)
            cnt += 1
print(cnt)