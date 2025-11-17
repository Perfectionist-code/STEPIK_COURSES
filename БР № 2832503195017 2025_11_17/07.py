k1 = 2
i1 = 10
nu1 = 30_000
t = 150
tr_sp = 140_000
N = 12
v1 = k1 * i1 * nu1 * t * N
t1_tr = v1 / tr_sp
print(t1_tr)
v2 = (k1 / 2) * (i1 / 5) * (nu1 / 1.5) * (t / 3) * N
t2_tr = v2 / tr_sp
print(t2_tr)
print(int((t1_tr-t2_tr)/3600))