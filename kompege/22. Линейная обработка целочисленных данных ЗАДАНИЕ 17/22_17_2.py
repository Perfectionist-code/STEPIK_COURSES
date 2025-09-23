with open('22_17_2.txt', 'r') as file:
    cnt = 0
    min_num = 10000
    for s in file:
        num = int(s)
        s = s.strip()
        if all((s[-1] == '2' or s[-1] == '7', not num % 3, not num % 11)):
            cnt += 1
            if num < min_num: min_num = num
print(cnt, min_num)
