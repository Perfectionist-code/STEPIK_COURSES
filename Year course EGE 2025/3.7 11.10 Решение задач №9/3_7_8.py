with open('9-161.txt', 'r') as file:
    cnt = 0
    for str_line in file:
        a, b, c, d = sorted(map(int, str_line.split()))
        if d < a + b + c and {a, b, c, d}.__len__() == 3:
            cnt += 1
            print(a, b, c, d)
print('Ответ:', cnt)
