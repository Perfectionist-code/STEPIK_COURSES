from itertools import permutations


def condition_1(*args) -> bool:
    return all(
        (args[0] == args[1] == args[2], args[3] == args[4], args[5] == args[6], args[0] != args[3], args[3] != args[5],
         args[5] != args[0]))


def condition_2(*args) -> bool:
    lst1 = sorted(args)[:4]
    for per in permutations(lst1, 4):
        if sum(per[:2]) % 2 and sum(per[2:]) % 2:
            return True
    return False


with open('3_24_6.txt', 'r') as file:
    res = 0
    for s in file:
        lst = list(map(int, s.split()))
        lst = sorted(lst, key=lambda x: (lst.count(x), x), reverse=True)
        if condition_1(*lst) and condition_2(*lst):
            res += sum(lst)
            print(lst)
print('------' * 10)
print('Ответ:', res)
