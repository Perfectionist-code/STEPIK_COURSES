from collections import Counter
lst_1 = [x for x in input().lower() if x not in ' .,!?:;-']
lst_2 = [x for x in input().lower() if x not in ' .,!?:;-']
print(('NO', 'YES')[Counter(lst_1) == Counter(lst_2)])

