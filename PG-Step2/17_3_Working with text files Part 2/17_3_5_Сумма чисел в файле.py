def make_digits(_str: str):
    for char in set(_str):
        if not char.isdigit():
            _str = _str.replace(char, ' ')
    return sum(map(int, _str.split()))


with open('nums.txt', encoding = 'utf-8') as file:
    res = 0
    for line in file:
        line = [int(x) if x.isdigit() else make_digits(x) for x in line.split() if not x.isalpha()]
        res += sum(line)
    print(res)
