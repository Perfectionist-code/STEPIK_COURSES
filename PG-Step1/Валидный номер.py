str1 = [int(x) if x.isdigit() else x for x in input()]
flag = True
match str1:
    case 7, '-', int(), int(), int(), '-', int(), int(), int(), '-', int(), int(), int(), int(): pass
    case int(), int(), int(), '-', int(), int(), int(), '-', int(), int(), int(), int(): pass
    case _:
        flag = False
print(('NO', 'YES')[flag])
