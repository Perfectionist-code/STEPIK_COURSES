from collections import Counter
print(('NO', 'YES')[Counter(input()) == Counter(input())])

# first_word = sorted(input())
# second_word = sorted(input())
#
# if first_word == second_word:
#     print("YES")
# else:
#     print("NO")

# first_word = input()
# second_word = input()
#
# first_word_dict = {}
# for c in first_word:
#     first_word_dict[c] = first_word_dict.get(c, 0) + 1
#
# second_word_dict = {}
# for c in second_word:
#     second_word_dict[c] = second_word_dict.get(c, 0) + 1
#
# if first_word_dict == second_word_dict:
#     print('YES')
# else:
#     print('NO')

# dcts = ({}, {})
# for d in dcts:
#     for c in input().lower():
#         d[c] = d.get(c, 0) + 1
#
# print(('NO', 'YES')[dcts[0] == dcts[1]])