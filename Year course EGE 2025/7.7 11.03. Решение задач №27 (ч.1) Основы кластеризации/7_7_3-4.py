from statistics import mean
from math import dist

clustersA = ([], [], [])
clustersB = ([], [], [], [])

with open('7_7_2_27a.txt', 'r') as file:
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if x < 6:
            clustersA[0].append((x, y))
        elif x > 6 and y > 22.5:
            clustersA[1].append((x, y))
        else:
            clustersA[2].append((x, y))
# print(sum(len(x) for x in clustersA), cnt)  # Проверка включения всех элементов в кластеры

with open('7_7_2_27b.txt', 'r') as file:
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if x < 15 < y:
            clustersB[0].append((x, y))
        elif x > 15 and y > 15:
            clustersB[1].append((x, y))
        elif x < 15 and y < 15:
            clustersB[2].append((x, y))
        elif x > 15 > y:
            clustersB[3].append((x, y))
# print(sum(len(x) for x in clustersB), cnt)  # Проверка включения всех элементов в кластеры

def centroid(kl):
    res = []
    for point in kl:
        dist_sum = sum(dist(point, p) for p in kl)
        res.append((dist_sum, point))
    return min(res)[1]

centrA = [centroid(k) for k in clustersA]
centrB = [centroid(k) for k in clustersB]
print(centrA)
print(centrB)

PxA = mean(x for x,y in centrA) * 10_000
PyA = mean(y for x,y in centrA) * 10_000
PxB = mean(x for x,y in centrB) * 10_000
PyB = mean(y for x,y in centrB) * 10_000
print(int(PxA), int(PyA))
print(int(PxB), int(PyB))