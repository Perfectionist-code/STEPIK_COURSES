tup = ('Кошка', 'Жираф', 'Верблюд', 'Страус')
vowel_letters = 'аеёиоуыэюя'.upper()
consonant_letters = 'бвгджзйклмнпрстфхцчшщ'.upper()
for i, word in enumerate(tup, 1):
    word = word.upper()
    if not ((word[3] in vowel_letters) <= (word[1] in consonant_letters)):
        print(i)
