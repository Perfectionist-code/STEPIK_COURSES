zodiac_signs = {

    "Телец": {

        4: range(21, 30 + 1),

        5: range(1, 20 + 1)

    },

    "Близнецы": {

        5: range(21, 32),

        6: range(1, 22)

    },

    "Лев": {

        7: range(23, 32),

        8: range(1, 24)

    }
}

date = input('Введите дату своего рождения в формате ДД.ММ.ГГГГ: ')
day, month, *year = map(int, date.split('.'))

for key, values in zodiac_signs.items():
    if month in values and day in values[month]:
        print('Поздравляем! Вы определили свой знак зодиака.\nВаш знак зодиака:', key)
        break
else:
    print('К сожалению, словарь знаков зодиака пока не полный. Дополните словарь и повторите попытку')


is day