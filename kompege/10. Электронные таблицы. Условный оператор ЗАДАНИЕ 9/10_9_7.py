with open('10_9_7.txt','r') as file:
    cnt = 0
    for s in file:
        lst = list(map(int, s. split()))
        if all((lst[0] == lst[2], lst[1] == lst[3], not lst[0]==lst[1]==lst[2]==lst[3])):
            print(*lst)
            cnt += 1
print(cnt)