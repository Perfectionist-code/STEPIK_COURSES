# poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
# poet_data_temp = list(poet_data)
# poet_data_temp[2] = 'Москва'
# poet_data = tuple(poet_data_temp)
#
# print(poet_data)

poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
poet_data = list(poet_data)
poet_data.pop()
poet_data = tuple(poet_data) + ('Москва',)
print(poet_data)