import random

n = int(1e6)
k = 0
s0 = 16
for _ in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)

    if y ** 4 + x ** 3 >= -2 and y ** 2 + 3 * x <= 2:
        k += 1

print((k / n) * s0)
