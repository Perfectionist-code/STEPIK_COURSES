def func(*args):
    x, y, z = args
    return (x * x + 2 * y - 3 * z) / (x * y * z)


print(func(int(input()), int(input()), int(input())))