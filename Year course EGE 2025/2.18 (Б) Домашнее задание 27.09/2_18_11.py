A = {12, 3, 4, 5, 8}
B = {3, 35, 6, 8, 9}
cnt = 0
for x in range(1, 100):
    if x in A and x in B:
        cnt += 1
        print(x)
print('Ответ:', cnt)