def f(n: int):
    if n < 3: return 2
    if n > 1 and n % 2: return 2 * f(n - 1) - f(n - 2) - 2
    return 2 * f(n - 2) - f(n - 1) + 2


print(f(17))
