from re import *

with open('24.txt') as file:
    s = file.readline()
print((ls:=len(s)))

num = r'([1-9][0-9]*)'
reg = fr'{num}([\+\*]{num})*'
reg = fr'(?=({reg}))'
ans = [x.group(1) for x in finditer(reg, s)]
res = [x.replace('*',' ').replace('+', ' ') for x in ans]
res= [len(x) for x in res if len(x.split()) <= 50]
print(max(res))

# ОТВЕТ: 428 3часа 40 мин