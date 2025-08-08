P = set(range(5, 16))
Q = set(range(10, 21))
lst_A = [set(range(a, b + 1)) for a, b in ([0, 7], [8, 15], [15, 20], [7, 20])]
for i, A in enumerate(lst_A, 1):
    for x in range(1, 100):
        if (x in P) and (x not in Q) and (x in A):
            break
    else:
        print(i, A)
