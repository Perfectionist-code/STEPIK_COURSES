# объявление функции
def get_month(language, number):
    ru_months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь',
                 'ноябрь', 'декабрь']
    en_months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                 'november', 'december']
    if language == 'ru':
        month = ru_months
    else:
        month = en_months
    return month[number - 1]


# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))
