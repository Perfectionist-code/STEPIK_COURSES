res = 0
for x in range(90):
    for y in range(50):
        if 11 * x + 20 * y == 1000:
            res += (x + y)
print(res)

