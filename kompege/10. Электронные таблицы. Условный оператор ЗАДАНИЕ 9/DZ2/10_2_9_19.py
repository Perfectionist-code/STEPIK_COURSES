from statistics import mean

with open('19_9_6925.txt') as file:
    cnt = 0
    for s in file:
        lst = [int(x) for x in s.split()]
        l_even = [x for x in lst if not x % 2]
        l_odd = [x for x in lst if x % 2]
        if not l_even:
            l_even = [0]
        if not l_odd:
            l_odd = [0]
        mean_nums = sorted((mean(l_even), mean(l_odd)))
        if (len(set(lst)) == len(lst) - 1) + (abs(mean_nums[0] - mean_nums[1]) > 50) == 1:
            print(*lst)
            cnt += 1
print('---' * 10)
print(cnt)
