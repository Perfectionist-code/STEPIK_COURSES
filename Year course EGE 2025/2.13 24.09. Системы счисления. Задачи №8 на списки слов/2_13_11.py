from itertools import product

i = 1
word = ''.join(sorted('ЛАЙМ'))
lst = []
for per in product(word, repeat=5):
    print(f'{i}. {(wrd := ''.join(per))}')
    i += 1
    lst.append(wrd)
for word in lst[::-1]:
    if all(['М' not in word, 'Л' not in word, 'ЙЙ' not in word]):
        res = word
        break
print(lst.index(word) + 1)
