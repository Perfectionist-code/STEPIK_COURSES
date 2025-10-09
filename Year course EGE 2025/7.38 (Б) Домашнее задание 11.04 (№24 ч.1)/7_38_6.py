with open('06.txt') as file:
    s = file.readline().replace('A', ' ').replace('E', ' ').split()
print(len(max(s, key=len)))
