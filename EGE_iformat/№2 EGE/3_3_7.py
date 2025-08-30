from functools import reduce

res = reduce(lambda a,b: int(a)*int(b), input())
print(res)