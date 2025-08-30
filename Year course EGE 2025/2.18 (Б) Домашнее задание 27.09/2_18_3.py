tup = ('Марина', 'Таня', 'Иван', 'Вадим')
vowel_letters = 'аеёиоуыэюя'.upper()
consonant_letters = 'бвгджзйклмнпрстфхцчшщ'.upper()
for word in tup:
    word = word.upper()
    if (word[0] in consonant_letters and word[-1] in consonant_letters) or (not word[-1] in consonant_letters):
        print(word)