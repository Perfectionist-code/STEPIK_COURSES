n, a, b = int(input()), complex(input()), complex(input())
res = a ** n + b ** n + a.conjugate() ** n + b.conjugate() ** (n + 1)
print(res)
