with open('20_9_6999.txt') as file:
    cnt = 0
    for s in file:
        lst = list(map(int, s.split()))
        multiple_3 = [x for x in lst if not x % 3]
        if len(multiple_3) == 3 and max(lst) - min(lst) <= sum(multiple_3):
            cnt += 1

print(cnt)
