def file_concatenation(name: str):
    with open(name, 'r', encoding = 'UTF-8') as input_file, open ('output.txt', 'a', encoding = 'UTF-8') as output_file:
        output_file.writelines(input_file)


# file_names_lst = [input() for _ in range(int(input()))]
file_names_lst = ['file_1.txt', 'file_2.txt', 'file_3.txt']
with open('output.txt', 'w', encoding = 'UTF-8') as makefile: pass
for file_name in file_names_lst:
    file_concatenation(file_name)