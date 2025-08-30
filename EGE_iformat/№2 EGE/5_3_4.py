lst = []
while (num := int(input())):
    if str(num).__len__() == 3:
        lst.append(num)
print(sum(lst))