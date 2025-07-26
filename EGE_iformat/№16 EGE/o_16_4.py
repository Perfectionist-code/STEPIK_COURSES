def f(n):
    if n <= 7:
        return n + 5
    return 3 * n * f(n - 2)

print(f(24))
