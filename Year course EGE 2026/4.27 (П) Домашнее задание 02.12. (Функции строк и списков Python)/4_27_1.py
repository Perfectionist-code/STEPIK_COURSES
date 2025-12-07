from collections import Counter

s = input()
c = Counter(s)
print(sorted(set(c.values()))[-2])
