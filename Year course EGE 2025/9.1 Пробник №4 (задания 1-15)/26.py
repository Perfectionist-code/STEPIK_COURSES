with open('26var01.txt') as file:
    n, m, k = map(int, file.readline().split())
    a = []
    for s in file:
        gr, vr = map(int, s.split())
        a.append((gr, vr))

T = [m + 1] * (k + 1)

for row, col in a:
    T[col] = row
print(T)

best_row = 0
best_col = 1

for

