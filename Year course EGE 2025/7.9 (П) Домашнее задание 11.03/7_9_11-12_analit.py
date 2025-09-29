from statistics import mean


def dist(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return max((abs(x2 - x1), abs(y2 - y1)))


clustersA = ([], [])
clustersB = ([], [], [])

with (open('7_9_6_27a.txt') as file):
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if y > 5:
            clustersA[0].append((x, y))
        else:
            clustersA[1].append((x, y))
# print((f:=[len(kl) for kl in clustersA]))
# print(sum(f), cnt)

with (open('7_9_6_27b.txt') as file):
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if x > 3:
            clustersB[0].append((x, y))
        elif y < -2:
            clustersB[1].append((x, y))
        else:
            clustersB[2].append((x, y))
print((f:=[len(kl) for kl in clustersB]))
print(sum(f), cnt)


def get_centroid(kl):
    res = []
    for point in kl:
        sum_dist = sum([dist(point, p) for p in kl])
        res.append((sum_dist, point))
    return min(res)[1]


centersA = [get_centroid(kl) for kl in clustersA]
centersB = [get_centroid(kl) for kl in clustersB]

PxA = int(mean([x for x, y in centersA]) * 10_000)
PyA = int(mean([y for x, y in centersA]) * 10_000)

PxB = int(mean([x for x, y in centersB]) * 10_000)
PyB = int(mean([y for x, y in centersB]) * 10_000)

print(PxA, PyA)
print(PxB, PyB)
