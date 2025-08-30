from itertools import product

i = 1
word = ''.join(sorted('ПОРТ'))
cnt = 0
for per in product(word, repeat=5):
    print(f'{i}. {(wrd := ''.join(per))}')
    i += 1
    if wrd in ('ТОПОР', 'РОПОТ'):
        cnt += 1
        if cnt == 1:
            start_num = i
        else:
            end_num = i
            break
print(end_num - start_num + 1)
