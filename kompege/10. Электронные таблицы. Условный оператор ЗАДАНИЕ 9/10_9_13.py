from itertools import permutations

with open('10_9_13.txt', 'r') as file:
    cnt = 0
    for s in file:
        lst = list(map(int, s.split()))
        if all([x[0] < sum(x[1:]) for x in permutations(lst)]):
            cnt += 1
print(cnt)
