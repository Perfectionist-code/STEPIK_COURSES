def fibonacci(n):
    if n == 1:
        return 0
    if n in (2,3):
        return 1
    return fibonacci(n-2) + fibonacci(n - 1)


print(fibonacci(int(input())))
