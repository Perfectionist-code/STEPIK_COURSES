from statistics import mean
from turtle import *
from random import random


def dist(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return max((abs(x2 - x1), abs(y2 - y1)))


data = []
with open('7_9_6_27b.txt') as file:
    for s in file:
        x, y = map(float, s.split())
        data.append((x, y))

clustersA = []
while data:
    kl = [data.pop()]
    for point in kl:
        n_points = [p for p in data if dist(point, p) < 0.5]
        for p1 in n_points:
            kl.append(p1)
            data.remove(p1)
    clustersA.append(kl)
print([len(kl) for kl in clustersA])

tracer(0)
up()
for kl in clustersA:
    color = random(), random(), random()
    for x, y in kl:
        goto(x * 40, y * 40)
        dot(3, color)
update()
mainloop()

def get_centroid(kl):
    res = []
    for point in kl:
        sum_dist = sum([dist(point, p) for p in kl])
        res.append((sum_dist,point))
    return min(res)[1]

centersA = [get_centroid(kl) for kl in clustersA]

PxA = int(mean([x for x, y in centersA]) * 10_000)
PyA = int(mean([y for x, y in centersA]) * 10_000)

print(PxA, PyA)
