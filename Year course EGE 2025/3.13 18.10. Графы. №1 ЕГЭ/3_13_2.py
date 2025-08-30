from itertools import permutations

table = '35 3457 1256 25 12347 3 35'
graph = 'КРПЛТ РС Р КМСП РСЛТ ПС ПС'

print(*'1234567')
graph_set = {frozenset(x) for x in graph.split()}
for per in permutations('КРМПЛТС'):
    new_graph = table
    for x, y in zip('1234567', per):
        new_graph = new_graph.replace(x, y)
    new_graph = {frozenset(x) for x in new_graph.split()}
    if new_graph == graph_set:
        print(*per)
