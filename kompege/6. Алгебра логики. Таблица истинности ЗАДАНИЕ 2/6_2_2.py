print(*'abcF')
for a in range(2):
    for b in range(2):
        for c in range(2):
            F = (a and not c) or (not b and not c)
            if F:
                print(a, b, c, int(F))
            if not F:
                print(a, b, c, int(F))
