from itertools import product

i = 1
word = ''.join(sorted('ФОКУС'))
lst = []
for per in product(word, repeat=5):
    print(f'{i}. {(wrd := ''.join(per))}')
    i += 1
    lst.append(wrd)
for word in lst[::-1]:
    if all(['Ф' not in word, word.count('У') == 2]):
        res = word
        break
print(lst.index(word) + 1)
