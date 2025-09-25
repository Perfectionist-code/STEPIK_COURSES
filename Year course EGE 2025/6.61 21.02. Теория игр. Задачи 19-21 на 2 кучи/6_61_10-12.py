from math import ceil


def f(s1, s2, m):
    if s1 + s2 <= 30: return m % 2 == 0
    if m == 0: return 0
    # print(m % 2, (s1, s2), '|' * 3, (s1 - 1, s2), (ceil(s1 / 2), s2), (s1, s2 - 1), (s1, ceil(s2 / 2)))
    h = (f(s1 - 1, s2, m - 1), f(ceil(s1 / 2), s2, m - 1), f(s1, s2 - 1, m - 1), f(s1, ceil(s2 / 2), m - 1))
    return any(h) if (m-1) % 2 == 0 else all(h)


print('19)', *[s for s in range(13, 100) if f(18, s, 2)])
print('20)', *[s for s in range(13, 100) if not f(18, s, 1) and f(18, s, 3)])
print('21)', *[s for s in range(13, 100) if not f(18, s, 2) and f(18, s, 4)])
