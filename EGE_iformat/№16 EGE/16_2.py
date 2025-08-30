def odd_factorial(n):
    if n == 1:
        return 1
    if not n % 2:
        return odd_factorial(n - 1)
    return n * odd_factorial(n - 2)


print(odd_factorial(int(input())))
