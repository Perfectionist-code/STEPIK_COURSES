from itertools import permutations

table = '13567 23467 312 426 517 6124 7125'
graph = 'АБВ БАВД ВАБГЕ ГВД ДБГЕК ЕДКВ КДЕ'

print(*'1234567')
graph = {x[0]: set(x[1:]) for x in graph.split()}
for per in permutations('АБВГДЕК'):
    new_graph = table
    for x, y in zip('1234567', per):
        new_graph = new_graph.replace(x, y)
    new_graph = {x[0]: set(x[1:]) for x in new_graph.split()}
    if graph == new_graph:
        print(*per)