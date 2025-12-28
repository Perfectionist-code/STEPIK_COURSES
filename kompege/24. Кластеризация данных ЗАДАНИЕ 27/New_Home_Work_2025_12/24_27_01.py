from math import dist
from statistics import mean

clustersA = ([], [])
clustersB = ([], [], [])

with open('01_27A_25439.txt') as file:
    for s in file:
        s = s.replace(',', '.')
        x, y = map(float, s.split())
        if x < 10 and 15 < y < 25:
            clustersA[0].append((x, y))
        elif y < 15:
            clustersA[1].append((x, y))
print(*(len(kl) for kl in clustersA))

with open('01_27B_25439.txt') as file:
    for s in file:
        s = s.replace(',', '.')
        x, y = map(float, s.split())
        if -1.8 < x < -1.2:
            clustersB[0].append((x, y))
        elif 0 > x > -1 and y < 5:
            clustersB[1].append((x, y))
        elif 0 > x > -1 and y > 5:
            clustersB[2].append((x, y))
print(*(len(kl) for kl in clustersB))


def get_centroid(kl):
    res = []
    for point in kl:
        dist_sum = sum(dist(point, p) for p in kl)
        res.append((dist_sum, point))
    return min(res)[1]


centroidsA = [get_centroid(kl) for kl in clustersA]

Px = abs(int(min(x for x, y in centroidsA) * 10_000))
Py = abs(int(min(y for x, y in centroidsA) * 10_000))

Q1 = min(len(kl) for kl in clustersB)
Q2 = max(len(kl) for kl in clustersB)

print('----' * 5)

print(Px, Py)
print(Q1, Q2)
