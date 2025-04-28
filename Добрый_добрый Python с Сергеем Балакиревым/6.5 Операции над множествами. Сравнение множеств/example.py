n = int(input())

sett = []
d = 2
while d * d <= n:
    if n % d == 0:
        sett.append(d)
        n //= d
    else:
        d += 1
if n > 1:
    sett.append(n)
print(sett)
print('ДА' if {2, 3, 5} <= set(sett) else 'НЕТ')