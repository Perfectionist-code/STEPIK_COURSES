def is_power_of_two(num: int) -> bool:
    if num == 1: return True
    i = 0
    while (deg := 2 << i) <= num:
        i += 1
        if deg == num:
            return True # Если хотите получить на выходе степень двойки, нужно поменять True на i
    return False


l = tuple(int(input()) for _ in range(int(input())))
# print(max(is_power_of_two(x) for x in l)) # Для определения максимальной степени двой двойки среди введённых числе
print(sum(is_power_of_two(x) for x in l))
