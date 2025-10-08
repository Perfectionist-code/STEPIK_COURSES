from statistics import mean

clustersA = ([], [])
clustersB = ([], [], [])

with open('04_27_A_18314.txt', 'r') as file:
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if x < 23:
            clustersA[0].append((x, y))
        else:
            clustersA[1].append((x, y))
print(*[len(kl) for kl in clustersA])
print(sum([len(kl) for kl in clustersA]), cnt)

with open('04_27_B_18314.txt', 'r') as file:
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if x < -11:
            clustersB[0].append((x, y))
        elif -11 < x < 17:
            clustersB[1].append((x, y))
        else:
            clustersB[2].append((x, y))
print(*[len(kl) for kl in clustersB])
print(sum([len(kl) for kl in clustersB]), cnt)


def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2 - x1) + abs(y2 - y1)


def get_centroid(kl):
    res = []
    for point in kl:
        sum_dist = sum([dist(point, p) for p in kl])
        res.append((sum_dist, point))
    return min(res)[1]


print('-----' * 10)

centroidsA = [get_centroid(kl) for kl in clustersA]
centroidsB = [get_centroid(kl) for kl in clustersB]

PxA = int(abs(mean([x for x, y in centroidsA])) * 1000)
PyA = int(abs(mean([y for x, y in centroidsA])) * 1000)
PxB = int(abs(mean([x for x, y in centroidsB])) * 1000)
PyB = int(abs(mean([y for x, y in centroidsB])) * 1000)

print(PxA, PyA)
print(PxB, PyB)
