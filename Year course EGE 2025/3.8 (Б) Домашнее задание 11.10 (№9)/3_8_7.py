from itertools import permutations


def is_condition_2(*args) -> bool:
    for per in permutations(args, 4):
        a, b, c, d = per
        if a + b == c + d:
            return True
    return False


with open('3_8_7.txt', 'r') as file:
    cnt = 0
    for str_line in file:
        a, b, c, d = sorted(map(int, str_line.split()))
        if all((d < a + b + c, is_condition_2(a, b, c, d))):
            cnt += 1
            print(a, b, c, d)
print('Ответ:', cnt)
