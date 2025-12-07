s = input().split()
s = [x for x in s if s.count(x) > 1]
if s:
    print(max(s, key=lambda x: (len(x), s.index(x))))
else:
    print('-1')
