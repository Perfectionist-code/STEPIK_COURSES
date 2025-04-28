with open('lines.txt', encoding='utf-8') as file:
    lst = list(map(str.strip, file.readlines()))
    print(*filter(lambda x: len(x) == len(max(lst,key = len)), lst), sep = '\n')

# with open('lines.txt') as f:
#     max_len, longest = 0, []
#     for line in f:
#         line = line.rstrip('\n')
#         line_len = len(line)
#         if line_len == max_len:
#             longest.append(line)
#         elif line_len > max_len:
#             max_len, longest = line_len, [line]
#
# print('\n'.join(longest))