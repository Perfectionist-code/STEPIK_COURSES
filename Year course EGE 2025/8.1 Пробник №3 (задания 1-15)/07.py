from math import ceil, log2

size = 1920 * 1080
tr_sp = 5_200_000
t = 100 * 60
iz = 32
kz = 2
nuz = 44_100
t_video = 60
n_frame = 25 * t_video
v_zv = kz * iz * nuz * t_video
for i in range(1, 1000):
    v_frame = i * size
    v_video = v_frame * n_frame
    V = v_zv + v_video
    if V / tr_sp > t:
        print(2 ** (i - 1) + 1)
        break
