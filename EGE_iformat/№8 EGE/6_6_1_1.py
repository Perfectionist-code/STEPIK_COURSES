from itertools import product

cnt = 0
for prod in product('ПЕТР', repeat=5):
    print(*prod, sep='')
    cnt += 1
print(cnt)

# count = 0  # счётчик для подсчёта слов
# for a1 in 'ПЕТР':  # перебор значений для первой позиции в слове
#     for a2 in 'ПЕТР':  # для второй и т.д.
#         for a3 in 'ПЕТР':
#             for a4 in 'ПЕТР':
#                 for a5 in 'ПЕТР':
#                     word = a1 + a2 + a3 + a4 + a5  # составляем слово
#                     count += 1  # увеличиваем счётчик
# print(count) # вывод результата
