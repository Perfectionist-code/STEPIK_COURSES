# ввод данных
n, k = map(int, input().split())

# здесь продолжите программу
import math
_Cnk=math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
print(int(_Cnk))