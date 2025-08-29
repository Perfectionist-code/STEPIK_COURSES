from itertools import permutations

table = '126 215 367 46 526 613457 736'
graph = 'АБГ БАВ ВБГ ГАДВЕЖ ДГ ЕГЖ ЖГЕ'

print(*'1234567')
graph_dict = {x[0]: set(x[1:]) for x in graph.split()}
for per in permutations('АВБГДЕЖ'):
    new_graph = table
    for x, y in zip('1234567', per):
        new_graph = new_graph.replace(x, y)
    new_graph = {x[0]: set(x[1:]) for x in new_graph.split()}
    if new_graph == graph_dict:
        print(*per)


