# Подвиг 8. Объявите функцию, которая имеет один параметр, принимающий строку. Функция должна возвращать два значения в виде кортежа: переданную строку и ее длину.
#
# После объявления функции далее в программе прочитайте из входного потока строку с названиями городов, записанных через пробел. Сформируйте на основе прочитанной строки список cities из названий городов. Затем, используя генератор словарей и ранее объявленную функцию, сформируйте на основе списка cities словарь d в формате:
#
# d = {<город 1>: <число символов>, ..., <город N>: <число символов>}
#
# Выведите этот словарь в порядке возрастания длин строк с помощью команд:
#
# a = sorted(d, key=d.get)
# print(*a)
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.2.8
#
# Sample Input:
#
# Воронеж Лондон Тверь Омск Уфа
# Sample Output:
#
# Уфа Омск Тверь Лондон Воронеж

def check_city_length(_str):
    return _str, len(_str)


cities = [city_name for city_name in input().split()]
d = {x: y for x, y in (check_city_length(i) for i in cities)}
a = sorted(d, key=d.get)
print(*a)



# def twix(w):
#     return w, len(w)
# d = {k:v for k, v in map(twix, input().split())}
# a = sorted(d, key=lambda x: d[x])
# print(*a)


# a = sorted(input().split(), key=len)
# print(*a)
