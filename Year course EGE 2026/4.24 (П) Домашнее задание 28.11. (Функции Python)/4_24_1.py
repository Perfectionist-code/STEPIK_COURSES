def get_max_figure(num: int) -> int:
    return int(max(tuple(str(num))))


l = tuple(int(input()) for _ in range(int(input())))
print(sum(get_max_figure(x) for x in l))
