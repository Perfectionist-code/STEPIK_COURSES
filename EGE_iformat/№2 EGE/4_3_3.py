from operator import pow, mul


def oper(ls: list, op, k=2) -> list:
    return [op(x, k) for x in ls]


lst = [int(input()) for _ in range(3)]
if all((d := [x > 0 for x in lst])):
    print(*oper(lst, mul), sep='\n')
elif (s := sum(d)) == 2:
    print(*oper(lst, mul, 3), sep='\n')
elif s == 1:
    print(*oper(lst, pow), sep='\n')
else:
    print(*lst, sep='\n')
