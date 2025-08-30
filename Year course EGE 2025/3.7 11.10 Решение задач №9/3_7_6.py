with open('3_7_6.txt', 'r') as file:
    cnt = 0
    for str_line in file:
        a, b, c = sorted(map(int, str_line.split()))
        if a + b + c > 2 * c:
            cnt += 1
print('Ответ:', cnt)
