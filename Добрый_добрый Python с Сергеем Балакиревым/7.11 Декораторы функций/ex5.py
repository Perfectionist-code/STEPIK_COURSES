# Подвиг 5. Объявите функцию, которая принимает строку с кириллицей и латиницей и преобразовывает русские символы в латиницу, используя следующий словарь для замены русских букв на соответствующее латинское написание:
#
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
# Функция должна возвращать преобразованную строку. Замены делать без учета регистра (переданную строку перевести в нижний регистр - малые буквы). Небуквенные символы " : ;.,_" превращать в символ '-' (дефиса).
#
# Определите декоратор для этой функции, который несколько подряд идущих дефисов, превращает в один дефис. Полученная строка должна возвращаться при вызове декоратора. (Сам декоратор на экран ничего выводить не должен).
#
# Примените декоратор к первой функции и вызовите ее для строки s, прочитанной из входного потока командой:
#
# s = input()
# Результат работы декорированной функции отобразите на экране.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.11.5
#
# Sample Input:
#
# Python - это круто!
# Sample Output:
#
# python-eto-kruto!

import time
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

def translit_string_deco(func):
    def wrapper(*args, **kwargs):
        _str_lower = _str.lower()
        for char in _str_lower:
            if char in ':;.,_':
                _str_lower = _str_lower.replace(char, '-')
            if char in t:
                _str_lower = _str_lower.replace(char, t[char])
        return func(_str_lower)

    return wrapper


@translit_string_deco
def cut_dashes(_str):
    str1 = _str.replace(' ', '-')
    while '--' in str1:
        str1 = str1.replace('--', '-')
    return str1


_str = input()
# _str = 'Python - это круто!'
st = time.time_ns()

transliterated_str = cut_dashes(_str)
print(transliterated_str)
et = time.time_ns()
dt = et - st
print(dt)

# def remove(func):
#     def wrapper(stroka):
#         ls = func(stroka).replace('-', ' ').split()
#         return '-'.join(ls)
#     return wrapper
#
#
# @remove
# def convert(strings):
#     lst = [t.get(i, i) if i not in ':;.,_' else '-' for i in strings.lower()]
#     return ''.join(lst)
#
#
# s = input()
# print(convert(s))
