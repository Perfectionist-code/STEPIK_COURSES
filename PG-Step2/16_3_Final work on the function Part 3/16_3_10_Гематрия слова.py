def get_gematria(word: str):
    return sum([ord(x) - 65 for x in word.upper()])


words_lst = [input() for _ in range(int(input()))]

res = sorted(words_lst, key = lambda x: (get_gematria(x), x))
print(*res, sep = '\n')
