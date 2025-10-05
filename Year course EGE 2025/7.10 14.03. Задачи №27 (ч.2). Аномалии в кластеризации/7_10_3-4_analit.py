from math import dist
from statistics import mean

clustersA = ([], [])
clustersB = ([], [], [])

with open('7_10_2_27a.txt') as file:
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if 4 < x < 6.5:
            pass
        elif x < 4:
            clustersA[0].append((x, y))
        else:
            clustersA[1].append((x, y))
# print(*[len(kl) for kl in clustersA])
# print(sum([len(kl) for kl in clustersA]), cnt)

with open('7_10_2_27b.txt') as file:
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if x < 3 or x > 14.9:
            pass
        elif 7.6 < y < 8.2:
            pass
        elif x < 9 and y < 7.6:
            clustersB[0].append((x, y))
        elif   x > 9 and y < 7:
            clustersB[1].append((x, y))
        else:
            clustersB[2].append((x, y))
print(*[len(kl) for kl in clustersB])
print(sum([len(kl) for kl in clustersB]), cnt)

# from turtle import *
# from random import random
#
# tracer(0)
# up()
# screensize(3000, 3000)
# for kl in clustersB:
#     color = random(), random(), random()
#     for point in kl:
#         x, y = point
#         goto(x * 40, y * 40)
#         dot(3, color)
# home()
# update()
# mainloop()

def get_centroid(kl):
    res = []
    for point in kl:
        sum_dist = sum(dist(point, p) for p in kl)
        res.append((sum_dist, point))
    return min(res)[1]

centroidsA = [get_centroid(kl) for kl in clustersA]
centroidsB = [get_centroid(kl) for kl in clustersB]

PxA = int(mean([x for x, y in centroidsA]) * 100_000)
PyA = int(mean([y for x, y in centroidsA]) * 100_000)

PxB = int(mean([x for x, y in centroidsB]) * 100_000)
PyB = int(mean([y for x, y in centroidsB]) * 100_000)

print(PxA, PyA)
print(PxB, PyB)
