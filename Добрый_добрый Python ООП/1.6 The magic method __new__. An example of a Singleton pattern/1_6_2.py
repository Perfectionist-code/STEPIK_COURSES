class SingletonFive:
    __cnt = 0
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__cnt < 5:
            print(f'Создаем экземпляр класса №{cls.__cnt}', end=' : ')
            cls.__cnt += 1
            cls.__instance = super().__new__(cls)
            print(cls.__instance)
        return  cls.__instance

    def __init__(self, name):
        self.name = name

objs = [SingletonFive(str(n)) for n in range(10)] # эту строчку не менять

for i, obj in enumerate(objs, 1):
    print(f'{i}: Name is "{obj.name}" - {obj}')
