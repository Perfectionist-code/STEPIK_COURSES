with open('file_1.txt', 'r', encoding = 'UTF-8') as input_file, open ('answer.txt', 'w', encoding = 'UTF-8') as output_file:
    d = {}
    line = input_file.readline()
    for line in input_file:
        if line.strip() != 'GOATS':
            d.setdefault(line.strip(), 0)
        else:
            break
    for key in input_file:
        key = key.strip()
        d[key] += 1
    total_goats = sum(d.values())
    answer_lst = filter(lambda x: d.get(x) / total_goats > .07 ,d.keys())
    print(*sorted(answer_lst), sep = '\n', file = output_file)