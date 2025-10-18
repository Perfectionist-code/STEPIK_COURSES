with open('22_17_4.txt') as file:
    lst = []
    for x in file:
        x= int(x)
        if x % 13 == 7  and x % 7 and x % 11:
            lst.append(x)
print(max(lst) - min(lst), len(lst))
