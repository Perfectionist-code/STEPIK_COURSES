for k in (0, 1):
    for l in (0, 1):
        for m in (0, 1):
            for n in (0, 1):
                if not ((not k or m) <= (not l or m or n)):
                    print(k, l, m, n, sep='')
