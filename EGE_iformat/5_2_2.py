res = 0
for _ in range(int(input())):
    if (d := int(input())) % 13:
        res += d
print(res)