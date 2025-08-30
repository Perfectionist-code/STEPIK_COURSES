for x in range(1, 1000):
    if not ((not x % 30) <= (x % 45)):
        print(x)
        res = x
        break
print('Ответ:', res)
