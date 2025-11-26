k = 2
nu = 44_000
i = 16
t = 60
n = 32
tr_sp = 1_802_240
v_file = k * nu * i * t
v_pack = v_file * n
print(v_pack//tr_sp)
