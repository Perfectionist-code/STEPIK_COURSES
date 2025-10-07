from math import dist
from statistics import mean
from random import random
from turtle import *

data = []
clusters = []

with open('03_27.19b.txt', 'r') as file:
    for s in file:
        x, y = map(float, s.split())
        data.append((x, y))
while data:
    kl = [data.pop()]
    for point in kl:
        sosed = [p for p in data if dist(point, p) < 2]
        for p1 in sosed:
            kl.append(p1)
            data.remove(p1)
    clusters.append(kl)
print(*[len(kl) for kl in clusters])
clusters = [kl for kl in clusters if len(kl) > 20]
print(*[len(kl) for kl in clusters])

tracer(0)
screensize(3000, 3000)
up()
for kl in clusters:
    color = random(), random(), random()
    for point in kl:
        x, y = point
        goto(x * 5, y * 5)
        dot(3, color)
update()
mainloop()


def get_true_edge(kl):
    res = []
    for point in kl:
        sum_dist = sum([dist(point, p) for p in kl])
        res.append((sum_dist, point))
    return max(res)[1]


true_edges = [get_true_edge(kl) for kl in clusters]

Tx = int(mean([x for x, y in true_edges]) * 10_000)
Ty = int(mean([y for x, y in true_edges]) * 10_000)

print(Tx, Ty)
