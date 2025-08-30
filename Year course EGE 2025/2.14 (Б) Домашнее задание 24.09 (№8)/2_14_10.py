from itertools import product

consonant_letters = 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
vowel_letters = 'АЕЁИОУЫЭЮЯ'


def condition_1(word: str) -> bool:
    cnt_consonant_letters = 0
    cnt_vowel_letters = 0
    for letter in word:
        if letter in vowel_letters:
            cnt_vowel_letters += 1
        else:
            cnt_consonant_letters += 1
    return cnt_consonant_letters > cnt_vowel_letters


letters = ''.join(sorted('СОТКА'))
for i, per in enumerate(product(letters, repeat=5), 1):
    word = ''.join(per)
    print(f'{i}. {word}')
    if 'О' in word and condition_1(word):
        print('Ответ: ', i)
        break
