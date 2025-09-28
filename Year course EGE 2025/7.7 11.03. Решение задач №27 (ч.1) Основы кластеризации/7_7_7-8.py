from math import dist
from statistics import mean

clustersA = ([], [])
clustersB = ([], [], [])

with open('7_7_4_27a.txt', 'r') as file:
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if y < -2 * x + 4:
            clustersA[0].append((x, y))
        else:
            clustersA[1].append((x, y))
# print(sum(len(x) for x in clustersA), cnt)

with open('7_7_4_27b.txt', 'r') as file:
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if y > 5 / 4 * x + 2:
            clustersB[0].append((x, y))
        elif y > -2 * x + 20:
            clustersB[1].append((x, y))
        else:
            clustersB[2].append((x, y))


# print([len(x) for x in clustersB], cnt)

def get_centroid(kl):
    res = []
    for point in kl:
        sum_dist = sum((dist(point, p) for p in kl))
        res.append((sum_dist, point))
    return min(res)[1]


centroidA = [get_centroid(kl) for kl in clustersA]
centroidB = [get_centroid(kl) for kl in clustersB]

PxA = mean(x for x, y in centroidA) * 10_000
PyA = mean(y for x, y in centroidA) * 10_000

PxB = mean(x for x, y in centroidB) * 10_000
PyB = mean(y for x, y in centroidB) * 10_000

print(int(PxA), int(PyA))
print(int(PxB), int(PyB))
