import _operator


def is_top_parabola(*args):
    return _operator.neg(_operator.truediv(b, _operator.mul(2, a))), _operator.truediv(
        _operator.sub((_operator.mul(_operator.mul(4, a), c)), pow(b, 2)), _operator.mul(4, a))


a, b, c = (int(input()) for _ in range(3))
print(is_top_parabola(a, b, c))