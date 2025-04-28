_str = input()
with open('file_3.txt', 'w', encoding = 'UTF-8') as file:
    file.writelines(_str + '\n')
print(file.closed)