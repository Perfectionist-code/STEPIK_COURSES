from fnmatch import fnmatch


def is_true(num_str: str) -> bool:
    even_cnt = odd_cnt = 0
    for char in set(num_str):
        if int(char) % 2:
            odd_cnt += num_str.count(char)
        else:
            even_cnt += num_str.count(char)
    return odd_cnt == even_cnt


mask1 = '12*34?5'
divider = 21025
for i in range(divider, int(1e10 + 1), divider):
    if fnmatch(s := str(i), mask1) and is_true(s):
        print(i, i // divider)
