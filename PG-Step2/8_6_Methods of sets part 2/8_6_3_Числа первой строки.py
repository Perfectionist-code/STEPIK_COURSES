A, B = set(map(int, input().split())), set(map(int, input().split()))
print(*sorted(A-B))