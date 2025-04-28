# Подвиг 1. На вход программе подаются целые числа, записанные через пробел. Прочитайте эту строку и сохраните через какую-либо переменную.
#
# Напишите функцию, которая имеет один параметр, преобразовывает переданную ей строку в список чисел и возвращает их сумму.
#
# Определите декоратор для этой функции, который имеет один параметр start - начальное значение суммы.
# Примените декоратор со значением start=5 к функции и вызовите декорированную функцию для прочитанной строки. Результат (сумму) отобразите на экране.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.12.1
#
# Sample Input:
#
# 5 6 3 6 -4 6 -1
# Sample Output:
#
# 26

def start_sum(start):
    def func_decorator(func):
        def wrapper(*args, **kwargs):
            sum = start + func(_str)

            return sum

        return wrapper

    return func_decorator


@start_sum(5)
def get_sum(_str1):
    res = sum([int(x) for x in _str1.split()])
    return res


_str = input()
print(get_sum(_str))
