from statistics import mean
from math import dist
from turtle import *
from random import random

clusters = []

with open('01_27B_18678.txt') as file:
    data = []
    for s in file:
        s = s.replace(',', '.')
        x, y = map(float, s.split())
        data.append((x, y))

while data:
    kl = [data.pop()]
    for point in kl:
        sosed = [p for p in data if dist(p, point) < 1]
        for p1 in sosed:
            kl.append(p1)
            data.remove(p1)
    clusters.append(kl)

print(*[len(kl) for kl in clusters])
clusters = [kl for kl in clusters if len(kl) > 20]
print(*[len(kl) for kl in clusters])


# r = 40
# tracer(0)
# up()
# for kl in clusters:
#     color = random(), random(), random()
#     for x, y in kl:
#         goto(x * r, y * r)
#         dot(3, color)
# update()
# done()

def get_centroid(kl):
    res = []
    for point in kl:
        sum_dist = sum([dist(point, p) for p in kl])
        res.append((sum_dist, point))
    return min(res)[1]


centroids = [get_centroid(kl) for kl in clusters]

Px = int(mean([x for x, y in centroids]) * 100_000)
Py = int(mean([y for x, y in centroids]) * 100_000)

print(Px, Py)
