A = {31, 10, 40, 11, 43}
B = {14, 31, 40, 1, 12, 94}
C = {40, 12, 10, 1, 13}
cnt = 0
for x in range(1, 100):
    if (x in A) or (x in B) and (x not in C):
        cnt += 1
        print(x)
print('Ответ:', cnt)
