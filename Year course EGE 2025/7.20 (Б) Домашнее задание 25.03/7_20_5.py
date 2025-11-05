from math import prod

with open('05.txt') as file:
    lst = [int(x) for x in file]
min_el_end7 = min([x for x in lst if abs(x) % 10 == 7])
print(min_el_end7)
res = []
for tr in zip(lst, lst[1:], lst[2:]):
    if any((len(str(x).lstrip('-')) == 5 for x in tr)) and abs(pr:=prod(tr)) % abs(min_el_end7) == 0:
        res.append(pr)
        print(*tr)
print(len(res), max(res))
