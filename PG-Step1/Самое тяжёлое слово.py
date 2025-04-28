words = (x for x in (input() for _ in range(4)))
hardest_word = max(words, key = (lambda x: sum([ord(y) for y in x])))
print(hardest_word)

# print(max((x for x in (input() for _ in range(4))), key = (lambda x: sum([ord(y) for y in x]))))