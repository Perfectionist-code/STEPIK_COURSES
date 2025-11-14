# def f(s, m):
#     if s >= 29: return m % 2 == 0
#     if m == 0: return 0
#     if s % 2 == 0:
#         h = [f(s + 4, m - 1), f(s + 6, m - 1)]
#     else:
#         h = [f(s + s % 10, m - 1), f(s + 6, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
#
# print('19)', *[s for s in range(2, 26) if f(s, 2)])
# print('20)', *[s for s in range(2, 26) if f(s, 4)])
# print('21)', *[s for s in range(2, 26) if f(s, 5)])

def f(s, m):
    if s > 29: return m % 2 == 0
    if m == 0: return 0
    h = [f(s + (s % 10, 4)[s % 2 == 0], m - 1), f(s + 6, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print('19)', *[s for s in range(2, 26) if f(s, 2)])
print('20)', *[s for s in range(2, 26) if f(s, 4)])
print('21)', *[s for s in range(2, 26) if f(s, 5)])
