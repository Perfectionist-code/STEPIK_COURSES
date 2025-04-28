def get_decimal_number(ip: str):
    ip_lst = [int(x) for x in ip.split('.')]
    return sum(x * 256 ** (3 - i) for i, x in enumerate(ip_lst))


ip_lst = [input() for _ in range(int(input()))]

res = sorted(ip_lst, key = lambda x: (get_decimal_number(x), x))
print(*res, sep = '\n')


# ip_lst = [[int(x) for x in input().split('.')] for _ in range(int(input()))]
#
# for res in sorted(ip_lst):
#     print(*res, sep = '.')