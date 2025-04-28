A, B, C = [set([int(x) for x in input().split()]) for _ in range(3)]
print(*sorted(C - (A | B), reverse = True))