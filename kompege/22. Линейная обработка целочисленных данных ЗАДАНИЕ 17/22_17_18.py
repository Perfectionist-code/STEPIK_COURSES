lst = [int(x) for x in open('22_17_18.txt')]
res = []
cnt = 0
a = lst[0]
for i in range(1, len(lst)):
    b = lst[i]
    if (a % 9 == 0 and b % 9 != 0 and oct(b).endswith('3')) or (b % 9 == 0 and a % 9 != 0 and oct(a).endswith('3')):
        print(a, b)
        cnt += 1
        res.append(max(a, b))
    a = b
print('-----' * 10)
print(cnt, max(res))
