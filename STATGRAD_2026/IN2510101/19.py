def f(s, m):
    if s <= 505: return m % 2 == 0
    if m == 0: return 0
    h = (f(s - 3, m - 1), f(s // 5, m - 1))
    return any(h) if (m - 1) % 2 == 0 else all(h)


print('19:', max([s for s in range(506, 100000) if f(s, 2)]))  # 19: 12649
print('20:', *[s for s in range(506, 100000) if not f(s, 1) and f(s, 3)])  # 20: 2533 2534
print('21:', *[s for s in range(506, 100000) if not f(s, 2) and f(s, 4)])  # 21: 2536

# 3 часа 6 минут


