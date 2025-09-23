def condition(A, B, C) -> bool:
    return not (A > 0 and A % 10 == 9) and (B > 0 and B % 10 == 9) and not (C > 0 and C % 10 == 9)


with open('22_17_19.txt', 'r') as file:
    cnt = 0
    lst = []
    for s in file:
        lst.append(int(s))
max_sum = -40000
a = lst[0]
for i in range(1, len(lst) - 1):
    b = lst[i]
    c = lst[i + 1]
    if condition(a, b, c):
        print(a, b, c)
        cnt += 1
        if max_sum < (m := a + b + c):
            max_sum = m
    a = b
print(cnt, max_sum)
