from math import ceil, log2

k = len(range(100, 30010))
i = ceil(log2(k))
v_pack = ceil(10 * i / 8)
N = 8192
print('Ответ:', v_pack * N // 2 ** 10, 'Кбайт')
