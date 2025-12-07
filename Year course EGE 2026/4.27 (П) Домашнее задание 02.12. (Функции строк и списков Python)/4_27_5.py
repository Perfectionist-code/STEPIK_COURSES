s = input()
d = {x: (s.count(x), ord(x)) for x in "AEUIOY" if s.count(x) > 0}
d = min(d, key=lambda x: d[x])
print(s.replace(d, ''))
