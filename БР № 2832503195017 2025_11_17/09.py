with open('09.txt') as file:
    cnt = 0
    for s in file:
        lst = sorted(map(int, s.split()))
        if (lst[0] + lst[-1]) ** 3 > sum((x**3 for x in lst[1:-1])):
            cnt +=1
            print(*lst)
print(cnt)