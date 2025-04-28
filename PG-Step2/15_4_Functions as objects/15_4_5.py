from math import sin, sqrt


def func_choice(f):
    func_dict = {'квадрат': lambda x: pow(x, 2),
                 'куб': lambda x: pow(x, 3),
                 'корень': sqrt,
                 'модуль': abs,
                 'синус': sin
                 }
    return func_dict[f]


number = int(input())
func = input().lower()

print(func_choice(func)(number))

# from math import sin, sqrt
#
#
# def func_choice(f: str, n: int):
#     match f:
#         case 'квадрат':
#             return pow(n, 2)
#         case 'куб':
#             return pow(n, 3)
#         case 'корень':
#             return sqrt(n)
#         case 'модуль':
#             return abs(n)
#         case 'синус':
#             return sin(n)
#         case _:
#             print('Такая функция нам не известна')
#
#
# number = int(input())
# func = input().lower()
#
# print(func_choice(func, number))
