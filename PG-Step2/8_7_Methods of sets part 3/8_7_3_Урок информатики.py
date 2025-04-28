A, B, C = [set([int(x) for x in input().split()]) for _ in range(3)]
res = A & B
print(*sorted(res - (res & C), reverse = True))