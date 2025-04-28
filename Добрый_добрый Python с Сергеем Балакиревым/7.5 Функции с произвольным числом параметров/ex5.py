# Значимый подвиг 6. (Для закрепления предыдущего материала). Объявите в программе функцию с именем str_min, которая сравнивает две переданные строки (через два первых параметра) и возвращает минимальную из них (то есть, выполняется лексикографическое сравнение строк). Следом объявите еще две аналогичные функции:
#
# с именем str_min3 для поиска минимальной строки из трех переданных строк;
# с именем str_min4 для поиска минимальной строки из четырех переданных строк.
# Причем при реализации функций str_min3 и str_min4 следует использовать вызов (результат работы) функции str_min.
#
# P.S. Выполнять функции не нужно, только объявить.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.5.6

# def str_min(str1,str2) :
#     return min(str1,str2)
#
#
# def str_min3(str1,str2,str3) :
#     return min(str_min(str1,str2),str3)
#
#
# def str_min4(str1,str2,str3,str4) :
#     return min(str_min3(str1,str2,str3),str4)

# Супер решение
# str_min = str_min3 = str_min4 = min

def str_min(*args) :
    return min(args)


def str_min3(*args) :
    return str_min(*args)


def str_min4(*args) :
    return str_min(*args)


print(str_min4(4,0,-1,-10))