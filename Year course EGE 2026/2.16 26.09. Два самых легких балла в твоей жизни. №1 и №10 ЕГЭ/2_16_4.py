from itertools import permutations

table = '1457 246 3567 412 5136 6235 713'
graph = 'ABC BDA CEGA DFGB EFC FEGD GCFD'

print(*'1234567')
graph_dict = {x[0]: set(x[1:]) for x in graph.split()}
for per in permutations('ABCDEFG'):
    new_graph = table
    for x,y in zip('1234567', per):
        new_graph = new_graph.replace(x,y)
    new_graph = {x[0]: set(x[1:]) for x in new_graph.split()}
    if new_graph == graph_dict:
        print(*per)
