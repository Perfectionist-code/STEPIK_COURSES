with open('class_scores.txt', 'r', encoding = 'UTF-8') as input_file, open ('new_scores.txt', 'w', encoding = 'UTF-8') as output_file:
    for line in input_file:
        name, mark = line.split()
        print(name, str(min(int(mark) + 5, 100)), file = output_file)