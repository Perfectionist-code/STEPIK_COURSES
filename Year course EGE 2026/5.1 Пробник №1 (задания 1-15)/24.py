from re import *

with open('24_14_1729263744.txt') as file:
    s = file.readline()

reg = r'(QRP|RP|P){0,1}(SQRP)+(SQR|SQ|S){0,1}'
reg = fr'(?=({reg}))'
m = max((x.group(1) for x in finditer(reg, s)), key=len)
print(len(m), m)

# PSQRPSQRPSQRPSQRPSQRPSQRPSQRPSQRPSQRPSQRPSQRPSQRPSQR