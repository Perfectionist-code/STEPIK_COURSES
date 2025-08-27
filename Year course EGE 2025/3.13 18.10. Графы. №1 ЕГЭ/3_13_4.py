from itertools import permutations

table = '58 357 25 67 123 48 248 167'
graph = 'ГД ЕДВ ЕГБ ДА БВК ГАЖ АЖ КВ'

print(*'12345678')
graph_set = {frozenset(x) for x in graph.split()}
for per in permutations('АВБГДЕЖК'):
    new_graph = table
    for x, y in zip('12345678', per):
        new_graph = new_graph.replace(x, y)
    new_graph = {frozenset(x) for x in new_graph.split()}
    if new_graph.__eq__(graph_set):
        print(*per)
