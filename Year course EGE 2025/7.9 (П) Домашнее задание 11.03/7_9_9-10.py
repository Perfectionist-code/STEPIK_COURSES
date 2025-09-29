from statistics import mean
from math import dist

clustersA = ([], [], [], [])
clustersB = ([], [], [], [], [], [], [])

with open('7_9_5_27a.txt') as file:
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if x < 1 and y > 0:
            clustersA[0].append((x, y))
        elif x < 1 and y < 0:
            clustersA[1].append((x, y))
        elif x > 1 and y > 2:
            clustersA[2].append((x, y))
        else:
            clustersA[3].append((x, y))
# print([len(x) for x in clustersA])
# print(sum([len(x) for x in clustersA]), cnt)

with open('7_9_5_27b.txt') as file:
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if x < -4:
            clustersB[0].append((x, y))
        elif -4 < x < 1 and y > -3:
            clustersB[1].append((x, y))
        elif -4 < x < 1 and y < -3:
            clustersB[2].append((x, y))
        elif 1 < x < 6 and y > 1:
            clustersB[3].append((x, y))
        elif 1 < x < 6 and y < 1:
            clustersB[4].append((x, y))
        elif x > 6 and y > 1:
            clustersB[5].append((x, y))
        else:
            clustersB[6].append((x, y))


# print([len(x) for x in clustersB])
# print(sum([len(x) for x in clustersB]), cnt)

def get_isolated_point(kl):
    res = []
    for point in kl:
        sum_points = sum([1 for p in kl if dist(point, p) <= 1])
        res.append((sum_points, point))
    return min(res)[1]


isolated_pointsA = [get_isolated_point(kl) for kl in clustersA]
isolated_pointsB = [get_isolated_point(kl) for kl in clustersB]

PxA = abs(int(mean([x for x, y in isolated_pointsA]) * 100_000))
PyA = abs(int(mean([y for x, y in isolated_pointsA]) * 100_000))

PxB = abs(int(mean([x for x, y in isolated_pointsB]) * 100_000))
PyB = abs(int(mean([y for x, y in isolated_pointsB]) * 100_000))

print(PxA, PyA)
print(PxB, PyB)
