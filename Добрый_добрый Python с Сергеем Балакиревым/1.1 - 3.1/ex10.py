a = input()
b, c = map(str, a.split())
c_1 = b in c
c_2 = b == c
c_3 = b > c
c_4 = b < c
print(c_1,c_2,c_3,c_4, sep = ' ')