file = open('17_2_4_numbers.txt', encoding = 'UTF-8')
print(sum(map(int, file.readlines())))
file.close()
