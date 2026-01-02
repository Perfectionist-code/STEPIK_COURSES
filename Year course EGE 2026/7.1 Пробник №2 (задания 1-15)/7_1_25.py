cnt = 0
for n in range(200000, 1000000):
    flag = False
    if not '1' in str(n):
        for x in range(0, n + 1, 103):
            if x % 2:
                for i in range(1, 14):
                    if x + 3 ** i == n:
                        cnt += 1
                        print(n, i)
                        flag = True
                        break
            if flag:
                break
    if cnt == 5:
        break

# Используется для нахождения максимального показателя степени числа 3
# cnt = 0
# num = 1000000
# while num:
#     num //= 3
#     cnt +=1
# print(cnt)
