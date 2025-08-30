
print(*'xyzw')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                if not (not ((w or (not y)) and x) or (y == z)):
                    print(x, y, z, w)
