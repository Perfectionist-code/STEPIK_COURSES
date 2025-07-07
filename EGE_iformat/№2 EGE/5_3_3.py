h = int(input())  # высота в см
cube_h = 1
res = 0
cnt = 0
while res <= h:
    res += cube_h
    cnt += 1
    cube_h += 1
print(cnt)
