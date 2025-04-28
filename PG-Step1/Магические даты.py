# объявление функции
def is_magic(date):
    return int(date[:2]) * int(date[3:5]) == int(date[-2:] )

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))