with open('words.txt', encoding = 'UTF-8') as file:
    _str = file.read().strip().split()
max_len_word = len(max(_str, key = len))
max_len_words = filter(lambda x: len(x) == max_len_word, _str)

print(*max_len_words, sep = '\n')
