with open('numbers.txt', encoding='utf-8') as file:
    for line in file:
        res = sum(map(int, line.split()))
        print(res)