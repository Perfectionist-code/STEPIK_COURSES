match input():
    case str(a) if a.count('f') >= 1:
        print(*[a.index('f'), a.rindex('f') if a.count('f') > 1 else ''])
    case _:
        print('NO')