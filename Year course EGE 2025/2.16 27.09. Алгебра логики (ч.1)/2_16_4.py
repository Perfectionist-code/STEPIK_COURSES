tup = ('east', 'fast', 'rest', 'last')
vowel_letters = 'AEIOU'
consonant_letters = 'BCDFGHJKLMNPQRSTVWXYZ'
for i, word in enumerate(tup, 1):
    word = word.upper()
    if not ((word[0] in vowel_letters) <= (word[3] in vowel_letters)):
        print(i)
