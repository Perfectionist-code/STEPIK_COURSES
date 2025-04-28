A, B, C = [set([int(x) for x in input().split()]) for _ in range(3)]
D = set(range(11))
# print(A, B, C, sep = '\n')
# res = A & B
# print(A & B, B & C, A & C, sep = '\n')
# print()
print(*sorted(D - (A | B | C)))
