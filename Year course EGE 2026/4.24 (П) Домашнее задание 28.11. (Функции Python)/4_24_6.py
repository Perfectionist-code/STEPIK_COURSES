from datetime import date, timedelta

Y, M, D = int(input()), int(input()), int(input())

d = date(Y, M, D)
d1 = str(d + timedelta(1)).replace('-', ' ')
d2 = str(d - timedelta(1)).replace('-', ' ')
print(d1, d2, sep='\n')
