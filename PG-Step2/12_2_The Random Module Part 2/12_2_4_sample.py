from random import sample
res = sample(range(1000000,9999999), 100)
print(*res, sep = '\n')
print(len(set(res)))