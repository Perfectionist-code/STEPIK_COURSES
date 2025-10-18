with open('02.txt') as file:
    cnt = 0
    for s in file:
        lst = sorted(map(int, s.split()))
        if (lst[0] + lst[-1]) ** 2 > sum((x ** 2 for x in lst[1:-1])):
            cnt += 1
            print(*lst)
print('----' * 5)
print(cnt)
