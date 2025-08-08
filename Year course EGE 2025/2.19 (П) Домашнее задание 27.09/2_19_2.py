for k in (0, 1):
    for l in (0, 1):
        for m in (0, 1):
            for n in (0, 1):
                if ((k <= m) and (k <= (not m)) and ((not k) <= (m and (not l) and n))):
                    print(k, l, m, n, sep='')
