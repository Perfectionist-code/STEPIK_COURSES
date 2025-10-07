from statistics import mean
from turtle import *
from random import random

clusters = []
data = []


def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return max((abs(x2 - x1), abs(y2 - y1)))


with open('03_27B_18054.txt', 'r') as file:
    for s in file:
        x, y = map(float, s.split())
        data.append((x, y))

while data:
    kl = [data.pop()]
    for point in kl:
        sosed = [p for p in data if dist(point, p) < 0.5]
        for p1 in sosed:
            kl.append(p1)
            data.remove(p1)
    clusters.append(kl)
print(*[len(kl) for kl in clusters])

tracer(0)
up()
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
Px = int(mean([x for x, y in centroids]) * 10000)
Py = int(mean([y for x, y in centroids]) * 10000)

print(Px, Py)
