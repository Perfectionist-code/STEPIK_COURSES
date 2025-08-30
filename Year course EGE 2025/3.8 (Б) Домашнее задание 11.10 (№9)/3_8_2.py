with open('9-127.txt', 'r') as file:
    cnt = 0
    for str_line in file:
        a, b, c = map(int, str_line.split())
        if b ** 2 - 4 * a * c < 0:
            cnt += 1
            print(a, b, c)
print('Ответ:', cnt)
