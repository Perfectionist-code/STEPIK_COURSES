from string import ascii_lowercase

with open('03_24_1040.txt') as file:
    s = file.readline()
print((ls := len(s)))

for char in ascii_lowercase:
    s = s.replace(char, ' ')
s = s.split()
print(len(max(s,key=len)))
