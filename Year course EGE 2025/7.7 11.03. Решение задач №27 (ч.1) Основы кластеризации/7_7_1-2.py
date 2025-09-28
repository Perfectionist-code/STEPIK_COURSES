from math import dist
from statistics import mean
clustersA = ([], [])
clustersB = ([], [], [])

with open('7_7_1_27a.txt', 'r') as file:
    for s in file:
        x, y = map(float, s.split())
        if x < 1:
            clustersA[0].append((x, y))
        else:
            clustersA[1].append((x, y))
# print([len(x) for x in clusterA])
with open('7_7_1_27b.txt', 'r') as file:
    for s in file:
        x, y = map(float, s.split())
        if y < 4:
            clustersB[0].append((x, y))
        elif 4 < y < 7:
            clustersB[1].append((x, y))
        else:
            clustersB[2].append((x, y))
# print([len(x) for x in clusterB])

def centroid(kl):
    res = []
    for point in kl:
        sum_dist = sum(dist(point,p1) for p1 in kl)
        res.append((sum_dist,point))
    return min(res)[1]

centerA = [centroid(kl) for kl in clustersA]
centerB = [centroid(kl) for kl in clustersB]
# print(centerA)
# print('----'* 25)
# print(centerB)
PxA = mean([x for x, y in centerA]) * 10_000
PyA = mean([y for x, y in centerA]) * 10_000

PxB = mean([x for x, y in centerB]) * 10_000
PyB = mean([y for x, y in centerB]) * 10_000
print(int(PxA), int(PyA))
print(int(PxB), int(PyB))
