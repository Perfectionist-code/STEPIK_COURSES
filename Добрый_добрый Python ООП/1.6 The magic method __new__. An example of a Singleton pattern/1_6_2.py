# 1.6 Магический метод __new__. Пример паттерна Singleton
# 9 из 12 шагов пройдено
# 10 из 17 баллов  получено
# Видео-разбор подвига (решение смотреть только после своей попытки):
#
# YouTube: https://youtu.be/uE1uf7Qtbh4
# Смотреть на RuTube
# Подвиг 7. Объявите класс SingletonFive, с помощью которого можно было бы создавать объекты командой:
#
# a = SingletonFive(<наименование>)
# Здесь <наименование> - это данные, которые сохраняются в локальном свойстве name созданного объекта.
#
# Этот класс должен формировать только первые пять объектов. Остальные (шестой, седьмой и т.д.) должны быть ссылкой на последний (пятый) созданный объект.
#
# Создайте первые десять объектов класса SingletonFive с помощью следующего фрагмента программы:
#
# objs = [SingletonFive(str(n)) for n in range(10)]
# P.S. В программе на экран ничего выводить не нужно.

class SingletonFive:
    __cnt = 0
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__cnt < 5:
            print(f'Создаем экземпляр класса №{cls.__cnt}', end=' : ')
            cls.__cnt += 1
            cls.__instance = super().__new__(cls)
            print(cls.__instance)
        return cls.__instance

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]  # эту строчку не менять

for i, obj in enumerate(objs, 1):
    print(f'{i}: Name is "{obj.name}" - {obj}')
