with open('3_7_10.txt', 'r') as file:
    cnt = 0
    for str_line in file:
        a, b, c, d, e = sorted(map(int, str_line.split()))
        if {a, b, c, d, e}.__len__() == 5 and 3 * (a + e) >= 2 * (b + c + d):
            cnt += 1
            print(a, b, c, d, e)
print('Ответ:', cnt)
