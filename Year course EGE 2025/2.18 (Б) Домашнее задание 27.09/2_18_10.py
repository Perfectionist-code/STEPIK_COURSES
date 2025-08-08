A = {2, 12, 4, 1, 13}
B = {13, 35, 4, 1, 81, 9}
C = {35, 2, 10, 15, 13}
cnt = 0
for x in range(1, 100):
    if not ((x not in A) and (x not in B) or (x in C)):
        cnt += 1
        print(x)
print('Ответ:', cnt)