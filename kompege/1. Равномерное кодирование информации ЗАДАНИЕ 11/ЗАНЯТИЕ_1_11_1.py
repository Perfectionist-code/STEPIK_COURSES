from math import log2, ceil

symbols = 'ИНФОРМАТК'
i = ceil(log2(len(symbols)))
n = 15
v = ceil(n * i / 8)
N = 25
V = v * N
print('Ответ: ', V, 'байт')
