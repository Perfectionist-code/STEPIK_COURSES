print(*'xyzwF')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((not x and y) == z) and w
                if F:
                    print(x, y, z, w, int(F))
