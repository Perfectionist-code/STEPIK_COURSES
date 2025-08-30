from math import ceil, log2
n = 19
i = ceil(log2(n))
n_group = 9
v = n_group * i
print('Ответ: ', v, 'бит')

