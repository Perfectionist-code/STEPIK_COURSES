with open('01_26_813.txt') as file:
    free_space, n = map(int, file.readline().split())
    a = sorted([int(x) for x in file], reverse=True)
print(free_space)
cnt = 0
last_file_size = 0
for x, y in zip(a, a[::-1]):
    if free_space - x >= 0:
        free_space -= x
        last_file_size = x
        cnt += 1
    if free_space - y >= 0:
        free_space -= y
        last_file_size = y
        cnt += 1
print(cnt, last_file_size)
