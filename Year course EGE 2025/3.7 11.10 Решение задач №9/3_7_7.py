from itertools import permutations

with open('9-160.txt', 'r') as file:
    cnt = 0
    for str_line in file:
        a, b, c, d = sorted(map(int, str_line.split()))
        if d < a + b + c:
            for per in permutations((a,b,c,d), 4):
                if sum(per[:2]) == sum(per[2:]):
                    print(*per)
                    cnt += 1
                    break
print('Ответ:', cnt)
