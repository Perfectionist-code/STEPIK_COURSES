from statistics import mean


def condition_1(*args) -> bool:
    if len(set(args)) == len(args) - 2:
        if args[0] != args[2]:
            return True
    return False


def condition_2(*args):
    return mean(args[:4]) < mean(args[4:])


with open('3_22_6.txt', 'r') as file:
    cnt = 0
    for s in file:
        lst = list(map(int, s.split()))
        lst = sorted(lst, key=lambda x: (lst.count(x), x), reverse=True)
        if condition_1(*lst) and condition_2(*lst):
            cnt += 1
            print(f'{cnt}.', *lst)
print('--------' * 10)
print('Ответ:', cnt)
