from statistics import mean

clustersA = ([], [])
clustersB = ([], [], [])

with open('7_7_5_27a.txt', 'r') as file:
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if y > x + 3:
            clustersA[0].append((x, y))
        else:
            clustersA[1].append((x, y))
# print([len(kl) for kl in clustersA], cnt)

with open('7_7_5_27b.txt', 'r') as file:
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if y < -2.5:
            clustersB[0].append((x, y))
        elif x < 3 and y > -2.5:
            clustersB[1].append((x, y))
        elif x > 3 and y > -2.5:
            clustersB[2].append((x, y))
# print(sum(len(kl) for kl in clustersB), cnt)

def dist_ch(point1: tuple, point2: tuple):
    x1, y1 = point1
    x2, y2 = point2
    return max((abs(x2 - x1), abs(y2 - y1)))


def get_centr(kl):
    res = []
    for point in kl:
        sum_dist = sum([dist_ch(point, p) for p in kl])
        res.append((sum_dist, point))
    return min(res)[1]


centrA = [get_centr(kl) for kl in clustersA]
centrB = [get_centr(kl) for kl in clustersB]

PxA = mean([x for x, y in centrA]) * 10000
PyA = mean([y for x, y in centrA]) * 10000

PxB = mean([x for x, y in centrB]) * 10000
PyB = mean([y for x, y in centrB]) * 10000

print(int(PxA), int(PyA))
print(int(PxB), int(PyB))
