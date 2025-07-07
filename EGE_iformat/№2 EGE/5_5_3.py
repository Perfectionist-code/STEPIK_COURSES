print(*'xyzw')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                if (z <= w) and y and (not x):
                    print(x, y, z, w)