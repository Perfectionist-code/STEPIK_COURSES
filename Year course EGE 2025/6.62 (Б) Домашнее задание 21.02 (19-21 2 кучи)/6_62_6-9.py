def f(s1, s2, m):
    if s1 + s2 >= 77: return m % 2 == 0
    if m == 0: return 0
    h = (f(s1 + 3, s2, m - 1), f(s1 * 3, s2, m - 1), f(s1, s2 + 3, m - 1), f(s1, s2 * 3, m - 1))
    return any(h) if (m - 1) % 2 == 0 else all(h)


print('19)', *[s for s in range(1, 65) if f(12, s, 2)])
print('20)', *[s for s in range(1, 65) if not f(12, s, 1) and f(12, s, 3)])
print('20)', *[s for s in range(1, 65) if not f(12, s, 2) and f(12, s, 4)])
