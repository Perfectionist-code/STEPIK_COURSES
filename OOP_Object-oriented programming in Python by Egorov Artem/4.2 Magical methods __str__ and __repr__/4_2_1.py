class Person:
    def __init__(self, name: str, surname: str, gender='male'):
        self.name = name
        self.surname = surname
        self._gender = gender

    @property
    def _gender(self):
        return self.gender

    @_gender.setter
    def _gender(self, new_gender: str):
        if new_gender in ('male', 'female'):
            self.gender = new_gender
        else:
            print('Не знаю, что вы имели в виду? Пусть это будет мальчик!')
            self.gender = 'male'

    # def __str__(self):
    #     return (f'Граждан{('ин', 'ка')[self.gender == 'female']} {self.surname} {self.name}')

    def __str__(self):
        citizens = 'Граждан' + ('ин', 'ка')[self.gender == 'female']
        return (f'{citizens} {self.surname} {self.name}')

# p = Person('Chuck', 'Norris')
# print(p.name)
# print(p.surname)
# print(p.gender)
# print(p)
#
# p = Person('Оби-Ван', 'Кеноби', True)
# print(p.name)
# print(p.surname)
# print(p.gender)
# print(p)
#
# p = Person('Mila', 'Kunis', 'female')
# print(p.name)
# print(p.surname)
# print(p.gender)
# print(p)
