with open('10_24-337.txt') as file:
    s = file.readline()
print((ls := len(s)))
for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    s = s.replace(char, ' ')
s = s.split()
print(len(max(s, key=lambda x: len(x.lstrip('0')))))
