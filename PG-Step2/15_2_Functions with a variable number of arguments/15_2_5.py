def print_products(*args):
    res = list(filter(lambda x: isinstance(x, str) and x != '', args))
    if res:
        for i, food in enumerate(res):
            print(f'{i+1}) {food}')
    else:
        print('Нет продуктов')

print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
print_products([4], {}, 1, 2, {'Beegeek'}, '')