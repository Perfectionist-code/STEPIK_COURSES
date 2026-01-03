from math import dist
from random import random
from turtle import *

clusters = []
data = []
with open('03_27A_25441.txt') as file:
    for s in file:
        s = s.replace(',', '.')
        x, y = map(float, s.split())
        data.append((x, y))

while data:
    cluster = [data.pop()]
    for point in cluster:
        sosed = [p for p in data if dist(point, p) < 1]
        for p1 in sosed:
            cluster.append(p1)
            data.remove(p1)
    clusters.append(cluster)
print(*(len(kl) for kl in clusters))
clusters = tuple(kl for kl in clusters if len(kl) > 20)
print(*(len(kl) for kl in clusters))


# tracer(0)
# up()
# r = 10
# for kl in clusters:
#     color = random(), random(), random()
#     # print(color)
#     for x, y in kl:
#         goto(x * r, y * r)
#         dot(3, color)
# update()
# done()

def get_centroid(kl):
    res = []
    for point in kl:
        dist_sum = sum(dist(point, p) for p in kl)
        res.append((dist_sum, point))
    return min(res)[1]

centroids = tuple(get_centroid(kl) for kl in clusters)
Px = int(abs(centroids[0][0] - centroids[1][0]) * 10_000)
Py = int(abs(centroids[0][1] - centroids[1][1]) * 10_000)

print(Px, Py)