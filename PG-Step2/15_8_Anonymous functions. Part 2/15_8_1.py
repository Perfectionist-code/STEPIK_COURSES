func = lambda x: not x % 19 or not x % 13

print(func(19))
print(func(13))
print(func(20))
print(func(15))
print(func(247))
