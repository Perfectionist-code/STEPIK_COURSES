from decimal import Decimal as D
num1 = D(input())
num = D(num1).as_tuple()
print((max(num.digits) + min(num.digits), max(num.digits))[int(num1) == 0])