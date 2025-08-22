with open('3_7_5.txt', 'r') as file:
    cnt = 0
    for str_line in file:
        a, b, c = sorted(map(int, str_line.split()))
        if c - a > b:
            cnt += 1
print('Ответ:', cnt)
