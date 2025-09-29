from statistics import mean
from math import dist

clustersA = ([], [])
clustersB = ([], [], [])

with open('7_9_7_27a.txt') as file:
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if y > 4:
            clustersA[0].append((x, y))
        else:
            clustersA[1].append((x, y))
# print(f := [len(kl) for kl in clustersA])
# print(sum(f), cnt)

with open('7_9_7_27b.txt') as file:
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if y < -x + 8:
            clustersB[0].append((x, y))
        elif y > x - 2:
            clustersB[1].append((x, y))
        else:
            clustersB[2].append((x, y))


# print(f := [len(kl) for kl in clustersB])
# print(sum(f), cnt)

def get_centroid(kl):
    res = []
    for point in kl:
        sum_dist = sum([dist(point, p) for p in kl])
        res.append((sum_dist, point))
    return min(res)[1]


centroidsA = [get_centroid(kl) for kl in clustersA]
centroidsB = [get_centroid(kl) for kl in clustersB]
PxA = int(mean([x for x, y in centroidsA]) * 100_000)
PyA = int(mean([y for x, y in centroidsA]) * 100_000)
PxB = int(mean([x for x, y in centroidsB]) * 100_000)
PyB = int(mean([y for x, y in centroidsB]) * 100_000)

print(PxA, PyA)
print(PxB, PyB)
