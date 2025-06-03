class Building:
    def __init__(self, floors_number):
        self.floors_number = floors_number
        self.booking = {floor: None for floor in range(self.floors_number + 1)}

    def __setitem__(self, key, value):
        if 0 <= key <= self.floors_number:
            self.booking[key] = value
        else:
            raise ValueError(f'Этажа {key} в нашем здании не сущестует!\nВ здании всего {self.floors_number} этажей ☝️')

    def __getitem__(self, item):
        return self.booking[item]

    def __delitem__(self, key):
        if key in self.booking:
            self.booking[key] = None

# iron_building = Building(22)  # Создаем здание с 22 этажами
# iron_building[0] = 'Reception'
# iron_building[1] = 'Oscorp Industries'
# iron_building[2] = 'Stark Industries'
# try:
#     iron_building[23] = 'Stark Industries Co'
#     print(iron_building[23])
# except ValueError as ex:
#     print(ex)
# print(iron_building[2])
# del iron_building[2]
# print(iron_building[2])
