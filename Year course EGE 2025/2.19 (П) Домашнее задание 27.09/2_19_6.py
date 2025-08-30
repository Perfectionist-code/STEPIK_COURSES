P = set(range(2, 11))
Q = set(range(6, 15))
lst_A = [set(range(a, b + 1)) for a, b in ([0, 3], [3, 11], [11, 15], [15, 17])]
for i, A in enumerate(lst_A, 1):
    for x in range(1, 100):
        if not (((x in A) <= (x in P)) or (x in Q)):
            break
    else:
        print(i, A)
