d = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
    }
d_modif = {char: key * (i + 1) for key, value in d.items() for i, char in enumerate(value)}
# print(d_modif)
message = input().upper()
res = []
for char in message:
    if char in d_modif:
        res.append(d_modif[char])
print(''.join(res))