from statistics import mean
from math import dist
from turtle import *
from random import random

data = []
with open('7_9_7_27b.txt') as file:
    for s in file:
        x, y = map(float, s.split())
        data.append((x, y))

clustersA = []
while data:
    kl = [data.pop()]
    for point in kl:
        n_points = [p for p in data if dist(point, p) < .5]
        for p1 in n_points:
            kl.append(p1)
            data.remove(p1)
    clustersA.append(kl)
print([len(x) for x in clustersA])

tracer(0)
up()
for kl in clustersA:
    color = random(), random(), random()
    for x, y in kl:
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


centroidsA = [get_centroid(kl) for kl in clustersA]
PxA = int(mean([x for x, y in centroidsA]) * 100_000)
PyA = int(mean([y for x, y in centroidsA]) * 100_000)


print(PxA, PyA)


