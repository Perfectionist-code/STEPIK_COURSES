from math import dist
from statistics import mean
from turtle import *
from random import random

data = []
clusters = []

with open('7_10_3_27b.txt', 'r') as file:
    for s in file:
        x, y = map(float, s.split())
        data.append((x, y))

while data:
    kl = [data.pop()]
    for point in kl:
        sosed = [p for p in data if dist(point, p) < 1]
        for p1 in sosed:
            kl.append(p1)
            data.remove(p1)
    clusters.append(kl)
print(*[len(kl) for kl in clusters])
clusters = [kl for kl in clusters if len(kl) > 20]
#
# tracer(0)
# up()
# for kl in clusters:
#     color = random(), random(), random()
#     for point in kl:
#         x, y = point
#         goto(x * 25, y * 25)
#         dot(3, color)
# update()
# mainloop()

def get_max_min_dist():
    max_dist = -2 ** 23
    min_dist = 2 ** 23
    for i in range(len(clusters) - 1):
        for j in range(i + 1, len(clusters)):
            kl1 = clusters[i]
            kl2 = clusters[j]
            for point_kl1 in kl1:
                for point_kl2 in kl2:
                    if (d := dist(point_kl1, point_kl2)) > max_dist:
                        max_dist = d
                    if d < min_dist:
                        min_dist = d
    return min_dist, max_dist


min_max_dists = get_max_min_dist()
print(int(min_max_dists[0] * 10000), int(min_max_dists[1] * 10000))
