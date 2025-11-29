from math import ceil
tr_sp = 33_600
size = 240 * 1890
i = 8 * 8
v = ceil(size * i / 8)
t = v / (tr_sp / 8)
print(t)
