s = '>' + '1' * 14 + '2' * 20 + '3' * 25
while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s in s:
        s = s.replace('>1', '22>3', 1)
    if '>2' in s in s:
        s = s.replace('>2', '2>', 1)
    if '>3' in s in s:
        s = s.replace('>3', '11>2', 1)
print(s)
res = sum(map(int, s[:-1]))
print('Ответ:', res)
