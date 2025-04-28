# Подвиг 7. На вход программе подается натуральное число, которое может содержать только простые множители 1, 2, 3, 5 и 7 (любые из них, не обязательно все). Необходимо прочитать это число и разложить его на простые множители. Затем, проверить, содержит ли оно множители 2, 3 и 5 (обязательно все их, хотя бы один раз). Если это так, то вывести "ДА", иначе "НЕТ".
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/6/6.5.7
#
# Sample Input:
#
# 210
# Sample Output:
#
# ДА

N = input()
# set_1 = {2, 3, 5}
# set_2 = [1, N]
n = [int(x) for x in N]
print('ДА' if n[-1] == 0 and sum(n) % 3 == 0 else 'НЕТ')



# print(('НЕТ', 'ДА')[int(input()) % 30 == 0])

# n = int(input())
#
# sett = set()
# d = 2
# while d * d <= n:
#     if n % d == 0:
#         sett.add(d)
#         n //= d
#     else:
#         d += 1
# if n > 1:
#     sett.add(n)
#
# print('ДА' if {2, 3, 5} <= sett else 'НЕТ')

# n = int(input())
#
# sett = []
# d = 2
# while d * d <= n:
#     if n % d == 0:
#         sett.append(d)
#         n //= d
#     else:
#         d += 1
# if n > 1:
#     sett.append(n)
# print(sett)
# print('ДА' if {2, 3, 5} <= set(sett) else 'НЕТ')