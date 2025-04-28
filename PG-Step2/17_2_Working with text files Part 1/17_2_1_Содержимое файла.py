file_name = input()
file = open(file_name)
file_read_lst = [line.strip() for line in file.readlines()]
for line in file_read_lst:
    print(line)
file.close()
