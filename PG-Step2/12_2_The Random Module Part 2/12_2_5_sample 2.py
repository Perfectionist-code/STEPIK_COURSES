from random import sample
word = list(input().lower())
anagram = sample(word, len(word))
print(''.join(anagram))