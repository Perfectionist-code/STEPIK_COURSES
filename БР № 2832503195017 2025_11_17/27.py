from statistics import mean
from math import dist

clustersA = ([], [])
clustersB = ([], [], [])

with open('27_A_21930.txt') as file:
    for s in file:
        s = s.replace(',', '.')
        x, y = map(float, s.split())
        if y > 12:
            clustersA[0].append((x, y))
        else:
            clustersA[1].append((x, y))
print(*(len(kl) for kl in clustersA))

with open('27_B_21930.txt') as file:
    for s in file:
        s = s.replace(',', '.')
        x, y = map(float, s.split())
        if y < 10:
            clustersB[0].append((x, y))
        elif y > 10 and x < 17:
            clustersB[1].append((x, y))
        else:
            clustersB[2].append((x, y))
print(*(len(kl) for kl in clustersB))


def get_anticentroid(kl):
    res = []
    for point in kl:
        sum_dist = sum((dist(point, p) for p in kl))
        res.append((sum_dist, point))
    return max(res)[1]


anti_centroidsA = [get_anticentroid(kl) for kl in clustersA]
anti_centroidsB = [get_anticentroid(kl) for kl in clustersB]

PxA = int(mean((x for x, y in anti_centroidsA)) * 10_000)
PyA = int(mean((y for x, y in anti_centroidsA)) * 10_000)

PxB = int(mean((x for x, y in anti_centroidsB)) * 10_000)
PyB = int(mean((y for x, y in anti_centroidsB)) * 10_000)

print(PxA, PyA)
print(PxB, PyB)
