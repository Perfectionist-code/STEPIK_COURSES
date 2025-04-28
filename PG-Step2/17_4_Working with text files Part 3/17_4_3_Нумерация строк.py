with open('file_2.txt', 'r', encoding = 'UTF-8') as input_file, open ('file_3.txt', 'w', encoding = 'UTF-8') as output_file:
    for i, line in enumerate(input_file):
        print(f'{i + 1}) {line.strip()}', file = output_file)