def f(s1, s2, m):
    if s1 + s2 >= 123: return m % 2 == 0
    if m == 0: return 0
    h = (f(s1 + 1, s2, m - 1), f(s1 * 2, s2, m - 1), f(s1, s2 + 1, m - 1), f(s1, s2 * 2, m - 1))
    return any(h) if (m - 1) % 2 == 0 else all(h)


print('19)', *[s for s in range(1, 110) if f(13, s, 2)])
print('20)', *[s for s in range(1, 110) if not f(13, s, 1) and f(13, s, 3)])
print('20)', *[s for s in range(1, 110) if not f(13, s, 2) and f(13, s, 4)])
