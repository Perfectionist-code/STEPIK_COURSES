s = input().replace('A', ' ').replace('E', ' ')
cnt = 0
for char in 'BCDF':
    cnt += s.count(char + ' ')
print(cnt)