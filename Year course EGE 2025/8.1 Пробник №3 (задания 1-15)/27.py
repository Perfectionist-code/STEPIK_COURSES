from math import dist
from statistics import mean
from turtle import *
from random import random

data = []
clusters = []

with open('27A_1731931654.txt') as file:
    for s in file:
        x, y = map(float, s.split())
        data.append((x, y))

while data:
    kl = [data.pop()]
    for point in kl:
        sosed = [p for p in data if dist(point, p) <= 5.5]
        for p1 in sosed:
            kl.append(p1)
            data.remove(p1)
    clusters.append(kl)
print(*(len(kl) for kl in clusters))


tracer(0)
r = 5
screensize(5000, 5000)
up()
for kl in clusters:
    color = random(), random(), random()
    for x, y in kl:
        goto(x*r,y*r)
        dot(3, color)
update()
done()

def get_pirson_k(kl):
    x_mean = mean(x for x, y in kl)
    y_mean = mean(y for x, y in kl)
    ch = sum((x - x_mean) * (y - y_mean) for x, y in kl)
    zn = (sum(((x - x_mean) ** 2 for x, y in kl)) * sum(((y - y_mean) ** 2 for x, y in kl))) ** 0.5
    return ch / zn


kor_izm = [kl for kl in clusters if 0.9 <= abs(get_pirson_k(kl)) <= 1]
print(*kor_izm, sep='\n')
ravg = int(mean(get_pirson_k(kl) for kl in kor_izm) * 100000)

print(sum([len(kl)for kl in kor_izm]), ravg)
