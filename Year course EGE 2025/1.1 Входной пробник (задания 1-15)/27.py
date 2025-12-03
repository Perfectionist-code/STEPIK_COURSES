from optparse import make_option
from statistics import mean
from math import dist

clustersA = ([], [])
clustersB = ([], [], [])

with open('demo_2025_27_А.txt') as file:
    file.readline()
    for s in file:
        s = s.replace(',', '.')
        x, y = map(float, s.split())
        if x < 1:
            clustersA[0].append((x, y))
        else:
            clustersA[1].append((x, y))
print(*(len(kl) for kl in clustersA))

with open('demo_2025_27_Б.txt') as file:
    file.readline()
    cnt = 0
    for s in file:
        cnt += 1
        s = s.replace(',', '.')
        x, y = map(float, s.split())
        if x > 5:
            clustersB[0].append((x, y))
        elif x < 5 and y > 6:
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


centroidsA = tuple(get_centroid(kl) for kl in clustersA)
centroidsB = tuple(get_centroid(kl) for kl in clustersB)
PxA = int(mean(x for x, y in centroidsA) * 10_000)
PyA = int(mean(y for x, y in centroidsA) * 10_000)
PxB = int(mean(x for x, y in centroidsB) * 10_000)
PyB = int(mean(y for x, y in centroidsB) * 10_000)

print(PxA, PyA)
print(PxB, PyB)
