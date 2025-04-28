file = open('17_2_6_prices.txt', encoding = 'UTF-8')
lst = [line.split() for line in file]
lst = [int(number) * int(price) for name, number, price in lst]
print(sum(lst))
file.close()
