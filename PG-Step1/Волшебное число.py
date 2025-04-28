words = [input() for _ in range(4)]
smallest_string = min(words)
max_string = max(words)
res = (ord(smallest_string[-1]) * ord(max_string[-1])) ** 2
print(res)
