with open('9-246.txt', 'r') as file:
    cnt = 0
    for str_line in file:
        a, b, c, d = sorted(map(int, str_line.split()))
        if a + d <= b + c:
            cnt += 1
            print(a, b, c, d)
print('Ответ:', cnt)
