with open('17.txt') as file:
    a = [int(x) for x in file]
cnt = 0
max_sum = []
max_3_kr_6 = max(filter(lambda x: -1000 < x < -99 and abs(x) % 6 == 0, a))
for x, y in zip(a, a[1:]):
    if (x < 0) + (y < 0) == 1 and x + y > max_3_kr_6:
        print(x, y)
        cnt += 1
        max_sum.append(x ** 2 + y ** 2)
print('----' * 5)
print(cnt, max(max_sum))

# ОТВЕТ: 2553 2 часа 27 мин
