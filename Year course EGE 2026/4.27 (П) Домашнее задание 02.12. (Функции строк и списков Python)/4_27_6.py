s = input().split()
idx_max_len = s.index(max(s, key=len))
idx_min_len = s.index(min(s, key=len))
print(abs(idx_max_len - idx_min_len) - 1)
