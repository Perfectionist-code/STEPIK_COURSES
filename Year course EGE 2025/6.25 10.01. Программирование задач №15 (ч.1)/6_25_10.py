def f(x):
    B = 160 <= x <= 180
    return B <= ((x % 35 == 0) <= (x % a == 0))


cnt = 0
for a in range(1, 1000):
    if all(f(x) for x in range(1, 10000)):
        print(a)
        cnt += 1
print(cnt)
