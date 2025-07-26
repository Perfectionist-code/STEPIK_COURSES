def f(n):
    if n <= 4:
        return 1
    return n * f(n - 1)

print((f(80) - f(78)) // f(76))
