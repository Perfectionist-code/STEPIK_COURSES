s = '3' * 100
while any(('333' in s, '1111' in s)):
    if '333' in s:
        s = s.replace('333', '1', 1)
    else:
        s = s.replace('1111', '3', 1)
print(s)
