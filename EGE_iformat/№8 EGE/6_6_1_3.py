from itertools import permutations

cnt = 0
for per in permutations('01234567', 5):
    per = ''.join(per).lstrip('0')
    if all([per.__len__() == 5, '37' not in per, '73' not in per]):
        print(per)
        cnt += 1
print(cnt)

# count = 0 # счётчик для подсчёта чисел
# for a1 in '1234567': # перебор значений для первой цифры в числе (кроме 0)
#     for a2 in '01234567': # для второй и т.д.
#         for a3 in '01234567':
#             for a4 in '01234567':
#                 for a5 in '01234567':
#                     num = a1 + a2 + a3 + a4 + a5 # составляем число из 5 цифр
#                     if len(set(num)) == 5 and '37' not in num and '73' not in num: # проверка условий
#                         count += 1 # увеличиваем счётчик
# print(count) # вывод результата