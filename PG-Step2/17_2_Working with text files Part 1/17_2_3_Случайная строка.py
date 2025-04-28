from random import randrange
file = open('17_2_3_lines.txt', encoding = 'UTF-8')
file_read_lst = list(map(str.strip, file.readlines()))
print(file_read_lst[randrange(len(file_read_lst))])
file.close()
