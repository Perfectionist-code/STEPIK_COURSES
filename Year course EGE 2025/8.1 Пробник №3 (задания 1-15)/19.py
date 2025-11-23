def f(s1, s2, m, hod='0', kucha=0):
    if s1 + s2 <= 42: return m % 2 == 0
    if m == 0: return 0
    if hod == '-4' and kucha == 1:
        h = [f(s1, s2 - 4, m - 1, '-4', 2), f(s1 // 3, s2, m - 1, '//3', 1), f(s1, s2 // 3, m - 1, '//3', 2)]
    elif hod == '-4' and kucha == 2:
        h = [f(s1 - 4, s2, m - 1, '-4', 1), f(s1 // 3, s2, m - 1, '//3', 1), f(s1, s2 // 3, m - 1, '//3', 2)]
    elif hod == '//3' and kucha == 1:
        h = [f(s1 - 4, s2, m - 1, '-4', 1), f(s1, s2 - 4, m - 1, '-4', 2), f(s1, s2 // 3, m - 1, '//3', 2)]
    elif hod == '//3' and kucha == 2:
        h = [f(s1 - 4, s2, m - 1, '-4', 1), f(s1, s2 - 4, m - 1, '-4', 2), f(s1 // 3, s2, m - 1, '//3', 1), ]
    else:
        h = [f(s1 - 4, s2, m - 1, '-4', 1), f(s1, s2 - 4, m - 1, '-4', 2), f(s1 // 3, s2, m - 1, '//3', 1),
             f(s1, s2 // 3, m - 1, '//3', 2)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print('19)', *[s for s in range(2, 10000) if f(50, s, 2)])
print('20)', *[s for s in range(2, 10000) if not f(50, s, 1) and f(50, s, 3)])
print('21)', *[s for s in range(2, 10000) if not f(50, s, 2) and f(50, s, 4)])
