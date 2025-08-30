with open('9-150.txt', 'r') as file:
    cnt = 0
    for str_line in file:
        a, b, c = sorted(map(int, str_line.split()))
        if a ** 3 > 3 * b * c:
            cnt += 1
            print(a, b, c)
print('Ответ:', cnt)
