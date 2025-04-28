def pretty_print(data, side='-', delimiter='|'):
    res = ''
    for arg in data:
        res += f'{delimiter} {arg} '
    res += f'{delimiter}'
    _length = len(res) - 2
    side_str = f' {side * _length} '
    print(side_str, res, side_str, sep = '\n')


pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side = '*')
pretty_print(['abc', 'def', 'ghi'], delimiter = '#')
pretty_print(['abc', 'def', 'ghi'], side = '*', delimiter = '#')


# def pretty_print(data, side='-', delimeter='|'):
#     line = f" {delimeter} ".join(map(str, data))
#     print(' ' + side * (2 + len(line)))
#     print(delimeter + ' ' + line + ' ' + delimeter)
#     print(' ' + side * (2 + len(line)))
