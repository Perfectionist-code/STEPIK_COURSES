# Подвиг 1. На вход программе подается строка. Необходимо ее прочитать и найти в ней все индексы строкового фрагмента "ра". Выведите найденные индексы на экран в одну строчку через пробел. Если же фрагмент "ра" отсутствует в строке, то вывести -1.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.4.1
#
# Sample Input:
#
# Барабанщик бил бой в барабан
# Sample Output:
#
# 2 23

st = input()
if 'ра' not in st:
    print(-1)
else:
    for i, d in enumerate(st):
        if st[i-1].lower() + d.lower()  == 'ра':
            print(i-1, end = ' ')
