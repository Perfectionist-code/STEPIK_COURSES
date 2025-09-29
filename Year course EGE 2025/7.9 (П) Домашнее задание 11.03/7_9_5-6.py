from math import dist
from statistics import mean

clustersA = ([], [])
clustersB = ([], [], [])

with open('7_9_3_27a.txt') as file:
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if y > -x / 2 + 2:
            clustersA[0].append((x, y))
        else:
            clustersA[1].append((x, y))
# print([len(x) for x in clustersA])
# print(sum([len(x) for x in clustersA]), cnt)

with open('7_9_3_27b.txt') as file:
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if x < 0:
            clustersB[0].append((x, y))
        elif x >0 and y < 3.5:
            clustersB[1].append((x, y))
        else:
            clustersB[2].append((x, y))


# print([len(x) for x in clustersB])
# print(sum([len(x) for x in clustersB]), cnt)

def get_centroids(kl):
    res = []
    for point in kl:
        sum_dist = sum([dist(point, p) for p in kl])
        res.append((sum_dist, point))
    return min(res)[1]


centroidsA = [get_centroids(kl) for kl in clustersA]
centroidsB = [get_centroids(kl) for kl in clustersB]

PxA = int(mean([x for x, y in centroidsA]) * 10_000)
PyA = int(mean([y for x, y in centroidsA]) * 10_000)

PxB = int(mean([x for x, y in centroidsB]) * 10_000)
PyB = int(mean([y for x, y in centroidsB]) * 10_000)

print(PxA, PyA)
print(PxB, PyB)
