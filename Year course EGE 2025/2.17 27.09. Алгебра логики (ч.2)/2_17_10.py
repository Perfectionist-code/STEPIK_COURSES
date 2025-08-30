A = set(range(5, 18))
B = set(range(10, 22))
C = set(range(12, 30))
for x in (30, 9, 4):
    print((not (x in B)) and (not (x in A)) or (x in C))
