from math import dist
from statistics import mean

clustersA = ([], [])
clustersB = ([], [], [])
cnt = 0
with open('05_27A_22625.txt') as file:
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if y < 15:
            clustersA[0].append((x, y))
        else:
            clustersA[1].append((x, y))
print(*(l := [len(kl) for kl in clustersA]))
print(cnt, sum(l))
cnt = 0

with open('05_27B_22625.txt') as file:
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if y > 20:
            clustersB[0].append((x, y))
        elif y < 5:
            clustersB[1].append((x, y))
        elif 10 < y < 20:
            clustersB[2].append((x, y))
print(*(l := [len(kl) for kl in clustersB]))
print(cnt, sum(l))
print('----' * 10)


def get_centroid_ant(kl, func=min):
    res = []
    for point in kl:
        sum_dist = sum([dist(point, p) for p in kl])
        res.append((sum_dist, point))
    return func(res)[1]


centroidsA = [get_centroid_ant(kl) for kl in clustersA]
centroidsB = [get_centroid_ant(kl) for kl in clustersB]

anti_centroidsA = [get_centroid_ant(kl, max) for kl in clustersA]
anti_centroidsB = [get_centroid_ant(kl, max) for kl in clustersB]

PxA = abs(int(mean([x for x, y in centroidsA]) * 10_000))
PxB = abs(int(mean([x for x, y in centroidsB]) * 10_000))

SyA = abs(int(mean([y for x, y in anti_centroidsA]) * 10_000))
SyB = abs(int(mean([y for x, y in anti_centroidsB]) * 10_000))

print(PxA, SyA)
print(PxB, SyB)
