with open('9-114.txt', 'r') as file:
    cnt = 0
    for str_line in file:
        a, b, c = map(int, str_line.split())
        if a == b == c:
            cnt += 1
            print(a, b, c)
print('Ответ:', cnt)
