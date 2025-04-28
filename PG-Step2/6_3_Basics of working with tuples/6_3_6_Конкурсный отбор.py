report = tuple(tuple(input().split()) for _ in range(int(input())))

for tup in report:
    print(*tup)
print()
for res in filter(lambda x: int(x[1]) > 3, report):
    print(*res)