d = {1: 'AEILNORSTU',
     2: 'DG',
     3: 'BCMP',
     4: 'FHVWY',
     5: 'K',
     8: 'JX',
     10: 'QZ'}

game_dict = {value: key for key, _str in d.items() for value in _str}
res = 0
for char in input().upper():
    res += game_dict[char]
print(res)