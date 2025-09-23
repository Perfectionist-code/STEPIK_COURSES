def find_sum_numbers(l: list) -> int:
    r_sum = 0
    for num in l:
        if not num % 35:
            r_sum += sum(map(int, str(num)))
    return r_sum


def condition(*args) -> bool:
    args = sorted(args)
    if args[0] == args[1]:
        return False
    return all((args[1] > res_sum >= args[0], hex(args[0])[2:].endswith('ef')))


with open('22_17_20.txt', 'r') as file:
    lst = []
    for s in file:
        lst.append(int(s))
cnt = 0
a = lst[0]
res_sum = find_sum_numbers(lst)
print(res_sum)
couples = []
for i in range(1, len(lst)):
    b = lst[i]
    if condition(a, b):
        cnt += 1
        couples.append((a, b))
        print(a, b)
    a = b
print(cnt, sum(min(couples, key=sum)))
