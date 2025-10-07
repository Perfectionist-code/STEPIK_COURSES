from statistics import mean
from turtle import *
from random import random
from math import dist

clustersA = ([], [])
clustersB = ([], [], [], [], [])

with open('01_27_A_17916.txt', 'r') as file:
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if y > 8:
            clustersA[0].append((x, y))
        else:
            clustersA[1].append((x, y))
print(*[len(kl) for kl in clustersA])
print(sum([len(kl) for kl in clustersA]), cnt)

with open('01_27_B_17916.txt', 'r') as file:
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if y > 14:
            clustersB[0].append((x, y))
        elif 10 < y < 14:
            clustersB[1].append((x, y))
        elif 6 < y < 10:
            clustersB[2].append((x, y))
        elif 2 < y < 6:
            clustersB[3].append((x, y))
        else:
            clustersB[4].append((x, y))
print(*[len(kl) for kl in clustersB])
print(sum([len(kl) for kl in clustersB]), cnt)


def get_centroid(kl):
    res = []
    for point in kl:
        sum_dist = sum([dist(point, p) for p in kl])
        res.append((sum_dist, point))
    return min(res)[1]


centroidsA = [get_centroid(kl) for kl in clustersA]
centroidsB = [get_centroid(kl) for kl in clustersB]

PxA = int(mean([x for x, y in centroidsA]) * 10_000)
PyA = int(mean([y for x, y in centroidsA]) * 10_000)
PxB = int(mean([x for x, y in centroidsB]) * 10_000)
PyB = int(mean([y for x, y in centroidsB]) * 10_000)

print('----' * 5)
print(PxA, PyA)
print(PxB, PyB)
