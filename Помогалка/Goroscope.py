zodiac_signs = {
    "Телец": {4: range(21, 30 + 1), 5: range(1, 20 + 1)},
    "Близнецы": {5: range(21, 32), 6: range(1, 22)},
    "Лев": {7: range(23, 32), 8: range(1, 24)}
}
month_dict = {'ЯНВ': 1, 'ФЕВ': 2, 'МАР': 3, 'АПР': 4, 'МАЙ': 5, 'ИЮН': 6, 'ИЮЛ': 7, 'АВГ': 8, 'СЕН': 9, 'ОКТ': 10,
              'НОЯ': 11, 'ДЕК': 12}


def date_to_base(new_date: str, sep=' '):
    for sepr in '._*-':
        if sepr in new_date:
            sep = sepr
            break
    date = new_date.split(sep)
    if date[1].isalpha():
        date[1] = month_dict[date[1][:3].replace('Я', 'Й')]
    return map(int, date)


day, month, year = date_to_base(input('Введите дату своего рождения в формате ДЕНЬ МЕСЯЦ ГОД: ').upper())
print(day, month, year)

for key, values in zodiac_signs.items():
    if month in values and day in values[month]:
        print('Поздравляем! Вы определили свой знак зодиака.\nВаш знак зодиака:', key)
        break
else:
    print('К сожалению, словарь знаков зодиака пока не полный. Дополните словарь и повторите попытку')
