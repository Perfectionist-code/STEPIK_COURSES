with open('06.txt') as file:
    n = int(file.readline())
    a = sorted([int(x) for x in file], reverse=True)
lst = a[::-1]
resA = []
while len(lst) >= 9:
    cheque = lst[:8]
    lst = lst[8:]
    cheque.append(lst.pop())
    resA.append(tuple(cheque))
resA.append(tuple(lst))
s = 0
for tp in resA:
    s += sum(tp[:8])
print(s)
s2 = 0
for i, price in enumerate(a, 1):
    if i % 9:
        s2 += price
    else:
        continue
print(s2)