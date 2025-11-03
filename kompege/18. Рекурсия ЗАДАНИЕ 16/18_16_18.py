def f(n):
    global s
    s += n ** 2
    if n > 1:
        s += 2 * n + 1
        f(n - 2)
        f(n // 3)

s = 0
f(100)
print(s)
