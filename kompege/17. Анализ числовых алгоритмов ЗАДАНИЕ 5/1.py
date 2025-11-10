num = abs(int(input()))
num = list(map(int,str(num)))

print(num[0] * num[-1] - num[1])