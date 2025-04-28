# Подвиг 6. На вход программе подается целое положительное число a. Необходимо его прочитать и объявить генератор, который бы возвращал модули чисел в диапазоне [-a; a] (включительно), а затем еще один генератор, который бы вычислял кубы чисел (возведение в степень 3), возвращаемых первым генератором.
#
# Вывести в одну строчку через пробел первые четыре значения. (Гарантируется, что генератор выдает, как минимум четыре значения).
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.1.6
#
# Sample Input:
#
# 3
# Sample Output:
#
# 27 8 1 0

a = int(input())
gen = (abs(x) for x in range(-a, a + 1))
gen2= (x ** 3 for x in gen)
print(next(gen2), next(gen2), next(gen2), next(gen2))


# (lambda a: print(*(abs(x**3) for x in range(-a, a+1)[:4])))(int(input()))


# a = int(input())
# gen = (abs(i) for i in range(-a, a + 1))
# gen_cube = (i ** 3 for i in gen)
# [print(next(gen_cube), end=' ') for _ in range(4)]

