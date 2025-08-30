from itertools import permutations

table = '145 246 35 41256 51346 6245'
graph = 'АБ БАЕГВ ВБГ ГДЕБВ ДЕГ ЕБДГ'

print(*'123456')
graph = {x[0]: set(x[1:]) for x in graph.split()}
for per in permutations('АБВГДЕ'):
    new_graph = table
    for x, y in zip('123456', per):
        new_graph = new_graph.replace(x, y)
    new_graph = {x[0]: set(x[1:]) for x in new_graph.split()}
    if new_graph == graph:
        print(*per)
