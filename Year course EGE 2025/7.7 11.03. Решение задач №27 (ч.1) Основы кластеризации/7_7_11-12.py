from statistics import mean
from math import dist

clustersA = ([], [], [], [])
clustersB = ([], [], [], [], [], [], [])

with open('7_7_6_27a.txt', 'r') as file:
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if x < 1 and y > 0:
            clustersA[0].append((x, y))
        elif x < 1 and y < 0:
            clustersA[1].append((x, y))
        elif x > 2 and y > 2:
            clustersA[2].append((x, y))
        elif x > 2 and y < 2:
            clustersA[3].append((x, y))
# print([len(x) for x in clustersA])
# print(sum(len(x) for x in clustersA), cnt)

with open('7_7_6_27b.txt', 'r') as file:
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
        elif x > 6 and y < 1:
            clustersB[6].append((x, y))
# print([len(x) for x in clustersB])
# print(sum(len(x) for x in clustersB), cnt)


def get_guidance_point(kl):
    res = []
    for point in kl:
        sum_points = sum([1 for p in kl if dist(point, p) <= 1])
        res.append((sum_points, point))
    return max(res)[1]


guidance_pointsA = [get_guidance_point(kl) for kl in clustersA]
guidance_pointsB = [get_guidance_point(kl) for kl in clustersB]

PxA = int(abs(mean([x for x, y in guidance_pointsA])) * 100_000)
PyA = int(abs(mean([y for x, y in guidance_pointsA])) * 100_000)

PxB = int(abs(mean([x for x, y in guidance_pointsB])) * 100_000)
PyB = int(abs(mean([y for x, y in guidance_pointsB])) * 100_000)

print(PxA, PyA)
print(PxB, PyB)
