str_set = set()
for _ in range(3):
    str_set.add(input())
res = str_set.__len__()
if res == 1:
    res = 'EQUAL'
elif res == 3:
    res = 'DIFFERENT'
else: res = 'BINGO!'
print(res)