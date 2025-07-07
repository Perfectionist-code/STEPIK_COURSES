print(*'xyzwF')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                if (F := ((not w) and ((y or z) <= ((not x) and y)))):
                    print(x, y, z, w, int(F))
