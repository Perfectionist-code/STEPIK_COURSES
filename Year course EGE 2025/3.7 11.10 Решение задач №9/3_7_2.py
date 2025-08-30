with open('9-107.txt', 'r') as file:
    cnt = 0
    for str_line in file:
        a, b, c = map(int, str_line.split())
        if a == b == c == 60:
            cnt += 1
print('Ответ:', cnt)
