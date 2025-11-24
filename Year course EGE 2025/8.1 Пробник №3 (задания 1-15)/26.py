with open('26_3_1733758277.txt') as file:
    n = int(file.readline())
    a = sorted(int(x) for x in file)
# a = [9,13,850,875,900,925,950,975,1000,2025]
clusters = []
while a:
    kl = [a[0]]
    a.remove(a[0])
    sosed = [x for x in a if x - kl[0] <= 1000]
    for p1 in sosed:
        kl.append(p1)
        a.remove(p1)
    clusters.append(kl)
print(*clusters, sep='\n')
max_ignor = 0
cnt_reg_click = 0
for kl in clusters:
    if len(kl) >= 5:
        cnt_reg_click += 5
        ignor = len(kl) - 5
        if ignor > max_ignor:
            max_ignor = ignor
    else:
        cnt_reg_click += len(kl)
print(cnt_reg_click, max_ignor)