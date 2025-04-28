from string import digits

with open('file.txt', encoding = 'utf-8') as file:
    cnt_lines = 0
    cnt_words = 0
    cnt_letters = 0
    for line in file:
        cnt_lines += 1
        line = [x.strip('!&\'.\n,$:"#@?') for x in line.split()]
        cnt_words += len(line)
        temp = ''.join(filter(lambda x: not x.isdigit(), line))
        _set_nums = set(temp) & set(digits)
        if _set_nums:
            for char in _set_nums:
                temp = temp.replace(char, '')
        cnt_letters += len(temp)
print(f'''Input file contains:
{cnt_letters} letters
{cnt_words} words
{cnt_lines} lines''')
