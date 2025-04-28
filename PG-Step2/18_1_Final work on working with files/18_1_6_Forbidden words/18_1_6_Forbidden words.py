def change_forbidden_words(_str: str):
    _str_lower = _str.lower()
    for word in forbidden_words_lst:
        if word in _str_lower:
            _str_lower = _str_lower.replace(word, '*' * len(word))
    res = []
    for i, char in enumerate(_str_lower):
        if char != '*':
            res.append(_str[i])
        else:
            res.append('*')
    return ''.join(res)


file_name = input()
# file_name = 'stepik_copy.txt'
with open("forbidden_words.txt", "r", encoding="UTF-8") as file:
    forbidden_words_lst = file.read().strip().split()
with open(file_name, "r", encoding="UTF-8") as file:
    for line in file:
        print(change_forbidden_words(line.strip()))
