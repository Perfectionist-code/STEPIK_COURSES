with open('22_17_1.txt', 'r') as file:
    max_num = 0
    cnt = 0
    for s in file:
        num = int(s)
        if all((not num % 3, num % 7, num % 17, num % 19, num % 27)):
            cnt += 1
            if num > max_num: max_num = num
print(cnt, max_num)
