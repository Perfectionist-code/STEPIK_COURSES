from math import dist
from statistics import mean

clustersA = ([], [])
clustersB = ([], [], [])

with open('02_27A_25440.txt') as file:
    for s in file:
        s = s.replace(',', '.')
        x, y = map(float, s.split())
        if -3 < x < 0 and -2 < y < 3:
            clustersA[0].append((x, y))
        elif 0 < x < 3 and y > 8:
            clustersA[1].append((x, y))
print(*(len(kl) for kl in clustersA))

with open('02_27B_25440.txt') as file:
    for s in file:
        s = s.replace(',', '.')
        x, y = map(float, s.split())
        if -1.8 < x < -1.2:
            clustersB[0].append((x, y))
        elif -1 < x < 0 and y < 5:
            clustersB[1].append((x, y))
        elif -1 < x < 0 and y > 5:
            clustersB[2].append((x, y))
print(*(len(kl) for kl in clustersB))


def get_centroid(kl):
    res = []
    for point in kl:
        dist_sum = sum(dist(point, p) for p in kl)
        res.append((dist_sum, point))
    return min(res)[1]


centroidsA = [get_centroid(kl) for kl in clustersA]
centroidsB = [get_centroid(kl) for kl in clustersB]
Px = abs(int(max(x for x, y in centroidsA) * 10_000))
Py = abs(int(max(y for x, y in centroidsA) * 10_000))

Qx = abs(int(mean(x for x, y in centroidsB) * 10_000))
Qy = abs(int(mean(y for x, y in centroidsB) * 10_000))

print('----' * 5)

print(Px, Py)
print(Qx, Qy)
