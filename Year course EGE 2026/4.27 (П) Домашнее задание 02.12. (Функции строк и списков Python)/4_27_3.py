l = tuple(map(int, input().split()))
idx_max = l.index(max(l))
idx_min = l.index(min(l))
if idx_max < idx_min:
    idx_max, idx_min = idx_min, idx_max
print(sum(l[idx_min + 1:idx_max]))
