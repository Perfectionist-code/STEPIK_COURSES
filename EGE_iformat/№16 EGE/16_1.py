def product(n):
    if not n // 10:
        return n
    return n % 10 * product(n // 10)


# print(product(int(input())))
