def f(s1, s2, m):
    if s1 + s2 >= 67: return m % 2 == 0
    if m == 0: return 0
    h = (f(s1 + 1, s2, m - 1), f(s1 + s2, s2, m - 1), f(s1, s2 + 1, m - 1), f(s1, s2 + s1, m - 1))
    return any(h) if (m - 1) % 2 == 0 else all(h)


print('19)', *[s for s in range(1, 58) if f(9, s, 2)])
print('20)', *[s for s in range(1, 58) if not f(9, s, 1) and f(9, s, 3)])
print('21)', *[s for s in range(1, 58) if not f(9, s, 2) and f(9, s, 4)])
