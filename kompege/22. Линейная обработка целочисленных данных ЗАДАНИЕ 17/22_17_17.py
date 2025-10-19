with open('22_17_17.txt') as file:
    a = [int(s) for s in file]
nums_end_4 = [x for x in a if abs(x) % 10 == 4]
s_m_4 = min(nums_end_4) + max(nums_end_4)
ans = []
for x in zip(a, a[1:]):
    if sum(x) < s_m_4:
        ans.append(sum(x))
print(len(ans), max(ans))
