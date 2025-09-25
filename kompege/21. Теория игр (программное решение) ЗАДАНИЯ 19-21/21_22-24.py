from math import ceil


def f(s1, s2, m):
    if s1 + s2 <= 20: return m % 2 == 0
    if m == 0: return 0
    h = (f(s1 - 1, s2, m - 1), f(ceil(s1 / 2), s2, m - 1), f(s1, s2 - 1, m - 1), f(s1, ceil(s2 / 2), m - 1))
    return any(h) if (m - 1) % 2 == 0 else all(h)


print('19)', *[s for s in range(11, 100) if f(10, s, 2)])
print('20)', *[s for s in range(11, 100) if not f(10, s, 1) and f(10, s, 3)])
print('20)', *[s for s in range(11, 100) if not f(10, s, 2) and f(10, s, 4)])
