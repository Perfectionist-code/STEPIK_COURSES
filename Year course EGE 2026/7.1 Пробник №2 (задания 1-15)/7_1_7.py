size = 2000 * 1000
i = 25
v = size * i
size_compr = 800 * 700
i_compr = 15
v_compr = size_compr * i_compr
N = 40
print((v - v_compr) * N // 2 ** 13)
