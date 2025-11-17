from itertools import permutations

table = '125 2156 345 4357 5123467 6257 7456'
graph = 'АБК БАВК ВБГК ГВДК ДЕГК ЕДК КАБВГДЕ'

print(*'1234567')
graph = {x[0]: set(x[1:]) for x in graph.split()}

for per in permutations('АБВГДЕК'):
    new_graph = table
    for x, y in zip('1234567', per):
        new_graph = new_graph.replace(x, y)
    new_graph = {x[0]: set(x[1:]) for x in new_graph.split()}
    if new_graph == graph:
        print(*per)
