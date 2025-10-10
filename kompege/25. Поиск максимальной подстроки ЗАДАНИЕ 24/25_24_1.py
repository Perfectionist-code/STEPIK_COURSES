with open('01_24_2420.txt') as file:
    s = file.readline()
print((ls := len(s)))

for char in 'CD':
    s = s.replace(char, ' ')
s = s.split()
print(len(max(s,key=len)))
