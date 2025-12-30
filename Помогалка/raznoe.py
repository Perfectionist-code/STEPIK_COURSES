# maximum = int(input())
# for _ in range(4):
#     num = int(input())
#     if num > maximum:
#         maximum = num
#
# print(maximum * 2)

# minimum = 100
# for _ in range(5):
#     num = int(input())
#     if num < minimum:
#         minimum = num
#
# print(minimum)

# counter = 0
# for i in range(1, 11):
#     if i % 2 == 1:
#         counter = counter + 1
#
# print(counter)

# counter = 0
# for i in range(20, 26):
#     if i >= 10:
#         counter = counter + 1
#
# print(counter)

# print(list(map(str.capitalize, input().split())))

# print(input().lower())
# print(input().lower() == input().lower())
# print(list(map(str.lower, input().split())))

# print((s := input()) == s.lower() or s == s.capitalize())

# from math import acos, sqrt, pi
# x0, y0, x1, y1 = map(float, input().split())
# alpha = round(acos((x0 * x1 + y0 * y1) / sqrt(x0 ** 2 + y0 ** 2) / sqrt(x1 ** 2 + y1 ** 2)) / pi * 180, 1)

# print((100, 0)[bool(int(input()) % 7)])

# a, b, x = map(float, input().split())
# res_in = a <= x < b
# res_not_in = not (a <= x <= b)

# a, b, c, d, x = map(float, input().split())
# res_1 = a < x < b or c <= x <= d
# res_2 = not (a < x < b) and c <= x <= d
# res_3 = not (a < x < b) and not (c <= x <= d)

rect_width, rect_height, w, h = map(int, input().split())
total = (rect_width % w != 0) * (rect_height / h) + (rect_height % h != 0) * (rect_width / w) + (rect_width % w != 0 and rect_height % h != 0)
# total =((a:=(0,1)[bool(rect_width % w)]) * (rect_width // w) + (b:=(0,1)[bool(rect_height % h)]) * (rect_height // h) + a * b )
print(total)
