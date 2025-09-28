from statistics import mean
from math import dist

clustersA = ([], [])
clustersB = ([], [], [])

with open('7_7_7_27a.txt', 'r') as file:
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if y < 3:
            clustersA[0].append((x, y))
        else:
            clustersA[1].append((x, y))
# print([len(x) for x in clustersA])
# print(sum(len(x) for x in clustersA), cnt)

with open('7_7_7_27b.txt', 'r') as file:
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if y < -x + 8:
            clustersB[0].append((x, y))
        elif y > -x + 8 and y > x - 2:
            clustersB[1].append((x, y))
        elif y > -x + 8 and y < x - 2:
            clustersB[2].append((x, y))


# print([len(x) for x in clustersB])
# print(sum(len(x) for x in clustersB), cnt)


def get_centroid(kl):
    res = []
    for point in kl:
        sum_dist = sum([dist(point, p) for p in kl])
        res.append((sum_dist, point))
    return min(res)[1]


centroidsA = [get_centroid(kl) for kl in clustersA]
centroidsB = [get_centroid(kl) for kl in clustersB]

PxA = int(mean([x for x, y in centroidsA]) * 100000)
PyA = int(mean([y for x, y in centroidsA]) * 100000)

PxB = int(mean([x for x, y in centroidsB]) * 100000)
PyB = int(mean([y for x, y in centroidsB]) * 100000)

print(PxA, PyA)
print(PxB, PyB)
