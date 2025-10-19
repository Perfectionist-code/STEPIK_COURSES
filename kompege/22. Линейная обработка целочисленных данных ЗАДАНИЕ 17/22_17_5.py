def condition_1(n: int) -> bool:
    return f'{n:x}'.endswith('b')


def condition_2(n: int):
    return n % 7 == 0 and n % 13 != 0 and n % 6 != 0 and n % 19 != 0


with open('22_17_5.txt') as file:
    lst = [int(x) for x in file]
ans = []
for num in lst:
    if condition_1(num) and condition_2(num):
        ans.append(num)
print(sum(ans), len(ans))