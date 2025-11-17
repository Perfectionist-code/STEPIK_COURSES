with open('26_7456.txt') as file:
    n = int(file.readline())
    a = []
    for s in file:
        row, place = map(int, s.split())
        a.append((row, place))
a = set(a)
a = sorted(a)
hall = [[] for _ in range(n)]
for r_p in a:
    row, place = r_p
    hall[row - 1].append(place)

num_best_row = 0
cnt = 0
for i, row in enumerate(hall, 1):
    for p in zip(row, row[1:], row[2:]):
        if p[1] - p[0] == 6 and p[2] - p[1] == 6:
            print(i,p[1])
            num_best_row = i
            cnt += 1
print('----' * 10)
print(num_best_row, cnt)