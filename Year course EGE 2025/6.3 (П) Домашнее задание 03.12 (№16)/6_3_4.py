def f(n):
    if n == 0: return 0
    if n % 2: return 1 + f(n - 1)
    return f(n // 2)


cnt = 0
for i in range(1, 1001):
    if f(i) == 3:
        cnt += 1
print('Ответ:', cnt)
