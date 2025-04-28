with open('data.txt', encoding='utf-8') as file:
    lst = list(map(str.strip, file.readlines()))
    print(*lst[::-1], sep = '\n')