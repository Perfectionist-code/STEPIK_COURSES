from math import dist
from statistics import mean

clustersA = ([], [], [], [])
clustersB = ([], [], [], [], [])

with open('7_7_3_27a.txt') as file:
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if x > 16:
            clustersA[0].append((x, y))
        elif 11 < x < 14:
            clustersA[1].append((x, y))
        elif 7 < x < 10 and y < 14:
            clustersA[2].append((x, y))
        elif 7 < x < 10 and y > 14:
            clustersA[3].append((x, y))
# print(sum([len(k) for k in clustersA]), cnt)

with open('7_7_3_27b.txt') as file:
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if x < 6.5:
            clustersB[0].append((x, y))
        elif y > 10:
            clustersB[1].append((x, y))
        elif 5 < y < 8:
            clustersB[2].append((x, y))
        elif 24 < x < 28 and y <5:
            clustersB[3].append((x, y))
        elif x >28:
            clustersB[4].append((x, y))
# print(sum([len(k) for k in clustersB]), cnt)
# print([len(k) for k in clustersB], cnt)

def get_centroid(kl):
    res = []
    for point in kl:
        sum_of_dist = sum([dist(point, p) for p in kl])
        res.append((sum_of_dist, point))
    return min(res)[1]

centroidA = [get_centroid(kl) for kl in clustersA]
centroidB = [get_centroid(kl) for kl in clustersB]

PxA = mean(x for x,y in centroidA) * 10_000
PyA = mean(y for x,y in centroidA) * 10_000

PxB = mean(x for x,y in centroidB) * 10_000
PyB = mean(y for x,y in centroidB) * 10_000

print(int(PxA), int(PyA))
print(int(PxB), int(PyB))