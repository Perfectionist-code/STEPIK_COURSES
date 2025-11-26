from math import dist
from itertools import combinations
from turtle import *
from random import random

clastersA = ([], [])
clastersB = ([], [], [])

with open('27_A.txt') as file:
    file.readline()
    for s in file:
        s = s.replace(',', '.')
        x, y = map(float, s.split())
        if y > 13:
            clastersA[0].append((x, y))
        else:
            clastersA[1].append((x, y))
print(*(len(kl) for kl in clastersA))

with open('27_B.txt') as file:
    file.readline()
    cnt = 0
    for s in file:
        cnt += 1
        s = s.replace(',', '.')
        x, y = map(float, s.split())
        if 15 < y < 20:
            clastersB[0].append((x, y))
        elif 23 < x < 28:
            clastersB[1].append((x, y))
        elif 11 < x < 17 and 10 < y < 13.5:
            clastersB[2].append((x, y))
print(*(len(kl) for kl in clastersB))
print(sum(len(kl) for kl in clastersB), cnt)

tracer(0)
screensize(5000,5000)
r = 30
up()
for kl in clastersB:
    color = random(), random(), random()
    for point in kl:
        x, y = point
        goto(x * r, y * r)
        dot(3,color)
update()
mainloop()


def get_centroid(kl):
    res = []
    for point in kl:
        sum_dist = sum(dist(point, p) for p in kl)
        res.append((sum_dist, point))
    return min(res)[1]


def get_min_max_dist(kl1, kl2):
    res_min = []
    res_max = []
    for p1 in kl1: # берём точку из кластера 1
        dists_p1_kl2 = tuple(dist(p1, p2) for p2 in kl2) # вычисляем расстояния от точки p1 кластера 1 до каждой точки кластера 2
        res_min.append(min(dists_p1_kl2)) # добавляем в список минимальное расстояние из найденных
        res_max.append(max(dists_p1_kl2)) # добавляем в список максимальное расстояние из найденных
    return min(res_min), max(res_max)


centroidsA = tuple(get_centroid(kl) for kl in clastersA)
PxA = abs(int(sum(x for x, y in centroidsA) * 10_000))
PyA = abs(int(sum(y for x, y in centroidsA) * 10_000))
print('----' * 5)
print(PxA, PyA)
# print('----' * 5)
min_max_dists = [get_min_max_dist(kl1, kl2) for kl1, kl2 in combinations(clastersB, 2)]
# print(min_max_dists)
Q1 = int(min(min_max_dists, key=lambda x: x[0])[0] * 10_000)
Q2 = int(max(min_max_dists, key=lambda x: x[1])[1] * 10_000)
# print('----' * 5)
print(Q1, Q2)
print('----' * 5)
