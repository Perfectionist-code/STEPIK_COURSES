with open('9-114.txt', 'r') as file:
    cnt = 0
    for str_line in file:
        a, b, c = map(int, str_line.split())
        if all((a + b > c, a + c > b, b + c > a)):
            if any((a == b, a == c, b == c)):
                cnt += 1
print('Ответ:', cnt)
