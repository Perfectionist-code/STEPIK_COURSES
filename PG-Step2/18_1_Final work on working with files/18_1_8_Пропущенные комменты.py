# file_name = input()
file_name = 'test.txt'
with open(file_name, encoding='UTF-8') as file:
    previous_line = ''
    res_lst = []
    for line in file:
        if not previous_line.startswith("#") and line.startswith("def "):
            res_lst.append(line[line.index(' ') + 1:line.index('(')])
        previous_line = line
if res_lst:
    print(*res_lst, sep='\n')
else:
    print("Best Programming Team")
