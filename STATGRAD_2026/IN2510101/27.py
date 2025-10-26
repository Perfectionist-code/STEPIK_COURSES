# 3 часа 50 минут

from math import dist

clustersA = ([],[])
clustersB = ([],[],[])

with open('27_A.txt') as file:
    for s in file:
        x, y = map(float, s. split())
        if x < 30:
            clustersA[0].append((x,y))
        else:
            clustersA[1].append((x,y))
clustersA = sorted(clustersA, key=len)
print([len(kl) for kl in clustersA])


with open('27_B.txt') as file:
    for s in file:
        x, y = map(float, s. split())
        if x > 17 and y > 42:
            clustersB[0].append((x,y))
        elif x > 17  and y < 32:
            clustersB[1].append((x,y))
        else:
            clustersB[2].append((x, y))
# clustersB = sorted(clustersB, key=len)
print([len(kl) for kl in clustersB])

def get_centroid(kl):
    res = []
    for point in kl:
        dist_sum = sum([dist(point, p) for p in kl])
        res.append((dist_sum, point))
    return max(res)[1]

centroidsA = [get_centroid(kl) for kl in clustersA]
centroidsB = [get_centroid(kl) for kl in clustersB]

P1_A = int(sum(centroidsA[0])*10000)
P2_A = int(sum(centroidsA[1])*10000)

Qx_B = int(centroidsB[0][0]*10000)
Qy_B = int(centroidsB[1][1]*10000)

print(P1_A, P2_A)
print(Qx_B, Qy_B)




