# Подвиг 3. На вход программы поступает строка из целых чисел, записанных через пробел. Необходимо прочитать эту строку и сохранить в какой-либо переменной.
#
# Напишите функцию get_list с одним параметром, которая преобразовывает эту строку в список из целых чисел и возвращает его. Определите декоратор для функции get_list, который сортирует список чисел по возрастанию. Результат сортировки должен возвращаться в виде списка чисел при вызове декорированной функции.
#
# Вызовите декорированную функцию get_list и отобразите полученный отсортированный список lst командой:
#
# print(*lst)
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.11.3
#
# Sample Input:
#
# 8 11 -5 4 3 10
# Sample Output:
#
# -5 3 4 8 10 11
# from curses import wrapper


def decorator_sort(func):
    def wrapper(*args):
        lst = func(args)
        return sorted(lst)

    return wrapper


@decorator_sort
def get_list(*args):
    return [int(x) for x in _str.split()]

@decorator_sort
def get_list_5(*args):
    return [2 * int(x) + 5 for x in _str.split()]

_str = input()
# get_list = decorator_sort(get_list)
print(*get_list(_str))
print(*get_list_5(_str))



# def show_sorted(func):
#     return lambda *args, **kwards: sorted(func(*args, **kwards))
#
# @show_sorted
# def get_list(s):
#     return list(map(int, s.split()))
#
# print(*get_list(input()))
