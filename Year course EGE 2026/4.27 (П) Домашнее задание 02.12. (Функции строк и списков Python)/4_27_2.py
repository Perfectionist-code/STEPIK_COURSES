def is_arithmetic_progression(lst: list) -> bool:
    d = lst[1] - lst[0]
    return len(lst) > 2 and d > 0 and all(
        lst[i+1] - lst[i] == d for i in range(len(lst) - 1))


l = sorted(map(int, input().split()))
print(('no', 'yes')[is_arithmetic_progression(l)])
