cnt = 0
for a in (0, 1):
    for b in (0, 1):
        for c in (0, 1):
            for d in (0, 1):
                if (((a <= b) and c) or (d and (not d))):
                    cnt += 1
print(cnt)
