with open('02_24_2426.txt') as file:
    s = file.readline()
print((ls := len(s)))

for char in 'ABC':
    s = s.replace(char, ' ')
s = s.split()
print(len(max(s,key=len)))
