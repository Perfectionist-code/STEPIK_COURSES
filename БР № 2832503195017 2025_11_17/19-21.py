def f(s, m):
    if s >= 22: return m % 2 == 0
    if m == 0: return 0
    h = (f(s + 1, m - 1), f(s + 2, m - 1), f(s * 2, m - 1))
    return any(h) if (m - 1) % 2 == 0 else all(h)

print('19)', *[s for s in range(1,22) if f(s, 2)])
print('20)', *[s for s in range(1,22) if not f(s, 1) and f(s, 3)])
v_s = []
for step in range(2,20,2):
    v_s.extend([s for s in range(1,22) if f(s, step)])
# print('21)', *[s for s in range(1,22) if not f(s, 1) and f(s, 3)])
print(*v_s)
v_s = set(v_s)
print(*(res:=sorted(v_s)))
print(len(res))