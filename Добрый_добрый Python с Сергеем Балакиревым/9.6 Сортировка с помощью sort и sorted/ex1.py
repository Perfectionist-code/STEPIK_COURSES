# Подвиг 2. На вход программе поступают целые числа, записанные через пробел. Прочитайте эту строку с числами и преобразуйте ее сначала в список из целых чисел, а затем список в кортеж из целых чисел. То есть, в программе будет две разные коллекции: список и кортеж. Отсортируйте по возрастанию значений эти коллекции методом sort, если это возможно, а иначе - примените функцию sorted.
#
# На экран ничего выводить не нужно, только сформировать две отсортированные коллекции: lst (список) - результат сортировки списка; tp_lst (кортеж) - результат сортировки кортежа.
#
# P. S. На результаты сортировок обязательно должны ссылаться переменные с именами lst и tp_lst!
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.6.2
#
# Sample Input:
#
# -2 -1 8 11 4 5
# Sample Output:

s = input()
lst = [int(x) for x in s.split()]
lst_tp = tuple(int(x) for x in s.split())
lst.sort()
tp_lst = tuple(sorted(lst_tp))
print(lst)
print(tp_lst)

s = input()


# def get_sort(x):
#     try:
#         x.sort()
#         return x
#     except AttributeError:
#         return type(x)(sorted(x))
#
#
# lst = list(map(int, s.split()))
# tp_lst = tuple(map(int, s.split()))
#
#
# srt = get_sort(lst)
# tp_lst = get_sort(tp_lst)