file_name = input()
file = open(file_name)
file_read_lst = [line.strip() for line in file.readlines()]
print(file_read_lst[-2])
file.close()
