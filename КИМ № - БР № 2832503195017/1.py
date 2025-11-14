from itertools import permutations


table = '1347 2356 3124567 413 523 6237 7136'
graph = 'АБВГ БАГЕ ВАГ ГВАБЕДЖ ДЕГЖ ЕБГД ЖГД'

graph = {x[0]: set(x[1:]) for x in graph.split()}
print(*'1234567')

for per in permutations('АБВГДЕЖ'):
    new_graph = table
    for x, y in zip('1234567', per):
        new_graph = new_graph.replace(x, y)
    new_graph = {x[0]: set(x[1:]) for x in new_graph.split()}
    if new_graph == graph:
        print(*per)