from math import dist
from statistics import mean

clustersA = ([], [])
clustersB = ([], [], [])

with open('01_27_A.txt') as file:
    for s in file:
        x, y, h = map(float, s.split())
        h = int(h)
        if 50 <= x <= 150 and 150 <= y <= 250:
            clustersA[0].append((x, y, h))
        elif 350 <= x <= 450 and 250 <= y <= 350:
            clustersA[1].append((x, y, h))
print(*(len(kl) for kl in clustersA))

with open('01_27_B.txt') as file:
    for s in file:
        x, y, h = map(float, s.split())
        h = int(h)
        if -250 <= x <= -150 and -250 <= y <= -100:
            clustersB[0].append((x, y, h))
        elif -100 <= x <= 0 and 100 <= y <= 200:
            clustersB[1].append((x, y, h))
        elif 100 <= x <= 200 and -50 <= y <= 50:
            clustersB[2].append((x, y, h))
print(*(len(kl) for kl in clustersB))


def get_centoid(kl):
    res = []
    for point in kl:
        delivery_difficulty = sum(dist(point[:2], p[:2]) * p[2] for p in kl)
        res.append((delivery_difficulty, point))
    return min(res)[1][:2]


centroidsA = tuple(get_centoid(kl) for kl in clustersA)
centroidsB = tuple(get_centoid(kl) for kl in clustersB)

PxA = int(mean(x for x, y in centroidsA) * 100_000)
PyA = int(mean(y for x, y in centroidsA) * 100_000)

PxB = int(mean(x for x, y in centroidsB) * 100_000)
PyB = int(mean(y for x, y in centroidsB) * 100_000)

print(PxA, PyA)
print(PxB, PyB)
