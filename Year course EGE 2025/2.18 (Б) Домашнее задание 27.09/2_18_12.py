for x in range(1, 1000):
    if (not x % 24) and (not x % 10):
        print(x)
        res = x
        break
print('Ответ:', res)
