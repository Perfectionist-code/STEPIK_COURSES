lst = tuple(int(input()) for _ in range(int(input())))
lst_odd = tuple(filter(lambda x: abs(x) % 2, lst))
print(*lst_odd, sum(lst_odd),sep='\n')
