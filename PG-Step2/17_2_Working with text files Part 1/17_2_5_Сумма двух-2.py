file = open('17_2_5_nums.txt', encoding = 'UTF-8')
print(sum(map(int, file.read().split())))
file.close()
