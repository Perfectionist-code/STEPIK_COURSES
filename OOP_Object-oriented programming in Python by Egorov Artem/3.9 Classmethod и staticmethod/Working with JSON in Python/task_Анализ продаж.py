import json

with open('manager_sales.json') as file:
    d = json.load(file)

max_price_sum = 0
for manager in d:
    print(manager['manager']['first_name'], manager['manager']['last_name'], end=' ')
    amount_of_sales = 0
    for car in manager['cars']:
        amount_of_sales += car['price']
    print(amount_of_sales)
    print('-----' * 15)
    if amount_of_sales > max_price_sum:
        max_price_sum = amount_of_sales
        res = (manager['manager']['first_name'], manager['manager']['last_name'], max_price_sum)
print(*res)
