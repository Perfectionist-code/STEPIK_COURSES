n = int(input())
k = int(input())
lst = list(range(1, n + 1))
while len(lst) > 1:
    for i in range(1, k):
        temp = lst.pop(0)
        lst.append(temp)
    lst.pop(0)

print(*lst)

# a = str(bin(n))     # Переводим введённое число в двоичную форму счисления
# # print(a)
# mask = '0b1' + '0' * (len(a) - 3) + '0'     # создаём маску для переключения первого бита с 1 на 0
# # print(mask)
# res = int(a + '1', 2) ^ int(mask, 2)        # производим добавку одного бита справа к введённому числу и переключение первого бита в положение в положение выключено согласно созданной маске
#
# print(res)


