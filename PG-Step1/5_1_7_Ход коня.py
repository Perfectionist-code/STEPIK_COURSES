x1, y1, x2, y2 = [int(x) for x in (input() for i in range(4))]
if (abs(x1-x2) == 1 and abs(y1-y2) == 2) or (abs(x1-x2) == 2 and abs(y1-y2) == 1):
   print('YES')
else:
   print('NO')


# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# difference_product = (x1 - x2) * (y1 - y2)
#
# if difference_product == 2 or difference_product == -2:
#     print("YES")
# else:
#     print("NO")