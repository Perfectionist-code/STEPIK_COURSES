with open('9-127.txt', 'r') as file:
    cnt = 0
    for str_line in file:
        a, b, c = map(int, str_line.split())
        if not b ** 2 - 4 * a * c:
            cnt += 1
print('Ответ:', cnt)
