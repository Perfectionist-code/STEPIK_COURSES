from collections import Counter


def is_condition_2(*args) -> bool:
    a, b, c, d, e, f = args
    set_nums = set(args)
    if set_nums.__len__() == 4:
        _count = Counter(args)
        for num in set_nums:
            if _count[num] == 3:
                return True
            elif _count[num] == 2:
                return False
            elif _count[num] == 1:
                continue
    return False


with open('3_7_11.txt', 'r') as file:
    cnt = 0
    for str_line in file:
        a, b, c, d, e, f = sorted(map(int, str_line.split()))
        if any(((a + f) ** 2 > b ** 2 + c ** 2 + d ** 2 + e ** 2, is_condition_2(a, b, c, d, e, f))):
            cnt += 1
            print(a, b, c, d, e)
print('Ответ:', cnt)
