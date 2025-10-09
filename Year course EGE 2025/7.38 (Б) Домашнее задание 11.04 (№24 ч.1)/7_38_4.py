with open('04.txt') as file:
    s = file.readline().replace('C',' ').replace('F', ' ').split()
print(len(max(s, key=len)))