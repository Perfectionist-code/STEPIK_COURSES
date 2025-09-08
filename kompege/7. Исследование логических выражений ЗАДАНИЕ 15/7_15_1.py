for A in range(1, 3000):
    cnt = 0
    for x in (d:=range(1, 3000)):
        if ((not x % A) and (not x % 24) and x % 16) <= (x % A):
            cnt += 1
        else: break
    else:
        if cnt == len(d):
            print(A)
            break
