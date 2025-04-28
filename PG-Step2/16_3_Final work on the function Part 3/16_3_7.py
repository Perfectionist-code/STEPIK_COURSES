def add3(x):
    return x + 3


def mul7(x):
    return x * 7

def compose(f, g):
    def composed_function(x):
        return f(g(x))
    return composed_function


print(compose(mul7, add3)(1))
print(compose(add3, mul7)(2))
print(compose(mul7, str)(3))
print(compose(str, mul7)(5))

#
# def compose(f, g):
#     return lambda x: f(g(x))