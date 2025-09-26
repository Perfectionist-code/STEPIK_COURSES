with open('10_9_8.txt','r') as file:
    cnt = 0
    for s in file:
        lst = list(map(int, s. split()))
        if len(set(lst)) == 2:
            print(*lst)
            cnt += 1
print(cnt)