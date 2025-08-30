max_len = 0
for n in range(6, 1000):
    s = '57' * n
    while any(('575' in s, '7777' in s)):
        if '575' in s:
            s = s.replace('575', '77', 1)
        if '7777' in s:
            s = s.replace('7777', '5', 1)
    s_len = s.__len__()
    if s_len > max_len:
        max_len = s_len
print(max_len)
