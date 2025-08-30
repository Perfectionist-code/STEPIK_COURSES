def func(*args):
    s, r, t = args
    return s + s * r * t / 100


print(func(int(input()), int(input()), int(input())))