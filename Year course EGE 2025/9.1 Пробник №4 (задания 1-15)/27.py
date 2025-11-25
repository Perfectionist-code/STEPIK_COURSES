from math import dist
from statistics import mean

clustersA = ([], [])
clustersB = ([], [], [])

with open('27var1A.txt') as file:
    for s in file:
        s = s.replace(',', '.')
        x, y = map(float, s.split())
        if y > 15:
            clustersA[0].append((x, y))
        else:
            clustersA[1].append((x, y))
print(*(len(kl) for kl in clustersA))

with open('27var1B.txt') as file:
    for s in file:
        s = s.replace(',', '.')
        x, y = map(float, s.split())
        if x > 2:
            clustersB[0].append((x, y))
        elif y < 0:
            clustersB[1].append((x, y))
        else:
            clustersB[2].append((x, y))
print(*(len(kl) for kl in clustersB))


def get_centroid(kl):
    res = []
    for point in kl:
        sum_dist = sum(dist(point, p) for p in kl)
        res.append((sum_dist, point))
    return min(res)[1]


centroidsA = [get_centroid(kl) for kl in clustersA]
centroidsB = [get_centroid(kl) for kl in clustersB]

PxA = abs(int(mean(x for x, y in centroidsA) * 10_000))
PyA = abs(int(mean(y for x, y in centroidsA) * 10_000))

PxB = abs(int(mean(x for x, y in centroidsB) * 10_000))
PyB = abs(int(mean(y for x, y in centroidsB) * 10_000))

print(PxA, PyA)
print(PxB, PyB)
