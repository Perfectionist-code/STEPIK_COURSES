with open('3_8_1.txt', 'r') as file:
    cnt = 0
    for str_line in file:
        a, b, c = map(int, str_line.split())
        if a + b + c == 180 and any((a == b, b == c, a == c)):
            cnt += 1
            print(a, b, c)
print('Ответ:', cnt)
