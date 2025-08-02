from itertools import product

i = 1
word = ''.join(sorted('КОМПЬЮТЕР'))
lst = []
for per in product(word, repeat=5):
    print(f'{i}. {(wrd := ''.join(per))}')
    i += 1
    lst.append(wrd)
for word in lst[::-1]:
    if all([word[0] != 'Ь', word.count('К') == 2, (lst.index(word) + 1) % 2]):
        res = word
        break
print(lst.index(res) + 1)
