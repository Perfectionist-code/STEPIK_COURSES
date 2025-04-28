registration_number = [int(x) if x.isdigit() else x for x in input()]
cl = 'АВЕКМНОРСТУХ'
flag = True
match registration_number:
    case str(a), int(), int(), int(), str(b), str(c), '_', int(), int(), int() if a in cl and b in cl and c in cl: pass
    case str(a), int(), int(), int(), str(b), str(c), '_', int(), int() if a in cl and b in cl and c in cl: pass
    case _:
        flag = False
print(('NO', 'YES')[flag])


# s = input()
# flag = 'NO'
# correct_letters = 'АВЕКМНОРСТУХ'
#
# if 9 <= len(s) <= 10:
#     letters = s[0] + s[4:6]
#     digits = s[1:4] + s[7:]
#     underscore = s[6]
#
#     if digits.isdigit() and underscore == '_':
#         flag = 'YES'
#
#     for c in letters:
#         if c not in correct_letters:
#             flag = 'NO'
#             break
#
# print(flag)