def is_condition_1(*args) -> bool:
    if args[-1] > 0 > args[0]:
        cnt_pos = 0
        cnt_neg = 0
        for num in args:
            if num < 0:
                cnt_neg += 1
            elif num > 0:
                cnt_pos += 1
        return cnt_neg > cnt_pos
    return False


def is_condition_2(*args) -> bool:
    return abs(args[0]) > args[-1]


with open('3_9_5.txt', 'r') as file:
    cnt = 0
    for str_line in file:
        lst = sorted(map(int, str_line.split()))
        if all((is_condition_1(*lst), is_condition_2(*lst))):
            cnt += 1
            print(*lst)
print('Ответ:', cnt)