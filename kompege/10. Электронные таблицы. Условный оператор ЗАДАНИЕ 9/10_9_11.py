with open('10_9_11.txt', 'r') as file:
    cnt = 0
    for s in file:
        lst = sorted(map(int, s.split()))
        if sum(lst) == 180 and lst[-1] > 90:
            cnt += 1
print(cnt)
