tup = ('Олеся', 'Иван', 'Вадим', 'Таня')
vowel_letters = 'аеёиоуыэюя'.upper()
consonant_letters = 'бвгджзйклмнпрстфхцчшщ'.upper()
for i, word in enumerate(tup, 1):
    word = word.upper()
    if ((word[0] in consonant_letters) or (word[-1] in consonant_letters)) and (not (word[-1] in consonant_letters)):
        print(i)