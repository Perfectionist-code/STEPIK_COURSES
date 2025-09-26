with open('10_9_6.txt', 'r') as file:
    cnt = 0
    for s in file:
        lst = sorted(map(int, s.split()))
        if lst[1] -lst[0] == lst[2] -lst[1] and len(set(lst)) == 3:
            print(lst)
            cnt +=1
print(cnt)