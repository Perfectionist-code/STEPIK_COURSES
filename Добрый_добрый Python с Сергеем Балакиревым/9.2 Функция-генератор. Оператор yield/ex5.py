# Подвиг 5. Объявите функцию-генератор, которая бы возвращала простые числа. (Простое число - это натуральное число, которое делится только на себя и на 1). Выведите с помощью этой функции первые 20 простых чисел (начиная с 2) в одну строчку через пробел.


# put your python code here


def find_prime_numbers(*args):
    num = 2
    while True:
        _bool = True
        if num < 2:
            _bool = False
        else:
            for i in range(2, num // 2 + 1):
                if num % i == 0:
                    _bool = False
            if _bool:
                yield num
            num += 1


prime_number = find_prime_numbers()
for _ in range(20):
    print(next(prime_number), end = ' ')

# import sympy
# # def gen_simple():
# #     i = 1
# #     while True:
# #         yield sympy.prime(i)
# #         i += 1
# # g = gen_simple()
# # print(*(next(g) for _ in range(20)))
#
# print(sympy.prime(3))


# def is_prime(n):
#     d = 2
#     while d * d <= n and n % d != 0:
#         d += 1
#     return d * d > n
#
# def get_prime():
#     n = 2
#     while True:
#         if is_prime(n):
#             yield n
#         n += 1
#
# gen = get_prime()
#
# print(*(next(gen) for i in range(20)))