from statistics import mean

clustersA = ([], [])
clustersB = ([], [], [])

with open('27A_3_20217.txt') as file:
    for s in file:
        x, y = map(float, s.split())
        if y > 5:
            clustersA[0].append((x, y))
        else:
            clustersA[1].append((x, y))
print(*[len(kl) for kl in clustersA])

with open('27B_3_20217.txt') as file:
    for s in file:
        x, y = map(float, s.split())
        if x > 5:
            clustersB[0].append((x, y))
        elif x < 5 and y > 6:
            clustersB[1].append((x, y))
        else:
            clustersB[2].append((x, y))
print(*[len(kl) for kl in clustersB])


def get_centroid(kl):
    m_x = mean([x for x, y in kl])
    m_y = mean([y for x, y in kl])
    return (m_x, m_y)


centroidsA = [get_centroid(kl) for kl in clustersA]
centroidsB = [get_centroid(kl) for kl in clustersB]

PxA = int(mean([x for x, y in centroidsA]) * 10000)
PyA = int(mean([y for x, y in centroidsA]) * 10000)

PxB = int(mean([x for x, y in centroidsB]) * 10000)
PyB = int(mean([y for x, y in centroidsB]) * 10000)

print(PxA, PyA)
print(PxB, PyB)
