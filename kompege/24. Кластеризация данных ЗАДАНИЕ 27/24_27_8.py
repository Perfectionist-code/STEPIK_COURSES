from math import dist
from statistics import mean
from turtle import *
from random import random

data = []
clusters = []

with open('08_27B_18056.txt', 'r') as file:
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        data.append((x, y))
while data:
    kl = [data.pop()]
    for point in kl:
        sosed = [p for p in data if dist(point, p) < 0.8]
        for p1 in sosed:
            kl.append(p1)
            data.remove(p1)
    clusters.append(kl)
print(*[len(kl) for kl in clusters])
print(sum([len(kl) for kl in clusters]), cnt)
print('-----' * 5)
clusters = [kl for kl in clusters if len(kl) > 10]


up()
tracer(0)
for kl in clusters:
    color = random(), random(), random()
    for point in kl:
        x, y = point
        goto(x * 30, y * 30)
        dot(3, color)
update()
mainloop()

def get_centroid(kl):
    res = []
    for point in kl:
        sum_dist = sum([dist(point, p) for p in kl])
        res.append((sum_dist, point))
    return min(res)[1]


centroids = [get_centroid(kl) for kl in clusters]

Px = int(abs(mean([x for x, y in centroids]) * 100_000))
Py = int(abs(mean([y for x, y in centroids]) * 100_000))

print(Px, Py)
