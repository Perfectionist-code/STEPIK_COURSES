print(*'xyzwF')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                if not (F:=(not (y <= x)) or (y == w) or z):
                    print(x, y, z, w, int(F))
