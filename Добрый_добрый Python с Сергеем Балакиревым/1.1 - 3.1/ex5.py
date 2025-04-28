# ввод данных
n, m = map(int, input().split())

# здесь продолжите программу
inter_max = 20
total_peaple = int (n+m)
c = total_peaple/inter_max
import math
c = math.ceil(c)
print(c)
