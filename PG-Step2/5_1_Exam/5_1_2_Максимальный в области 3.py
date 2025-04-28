from sympy import flatten
n = int(input())
print(max(flatten([[int(x) for x in input().split()[-1:-i - 2:-1]] for i in range(n)])))




