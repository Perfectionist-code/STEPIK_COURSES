message = input().split()
d = {}
res = []
for word in message:
    if word not in d:
        d.setdefault(word, 1)
    else:
        d[word] += 1
    res.append(d[word])
print(*res)
