k = 2
nu = 44_000
i = 26
v_z = 18 * 2 * 13
t = 37 * 60 + 10
n = 11
V = k * nu * i * t + v_z * n
t_tr = V / (256 * 10 ** 6)
print(int(t_tr))
