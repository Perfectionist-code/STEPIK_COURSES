with open('22_17_16.txt') as file:
    a = [int(x) for x in file]

k_11 = [x for x in a if abs(x) % 11 == 0]
k_17 = [x for x in a if abs(x) % 17 == 0]
print(*((len(k_17), max(k_17)), (len(k_11), min(k_11)))[len(k_11) > len(k_17)])
