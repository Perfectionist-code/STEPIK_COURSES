from statistics import mean

with open('10.txt') as file:
    for s in file:
        l = list(map(int, s.split()))
        if all(l[i] > l[i + 1] for i in range(len(l) - 1)) and mean((l[0], l[-1])) > mean(l[1:-1]):
            print(*l)
            print(sum(l))
            break
