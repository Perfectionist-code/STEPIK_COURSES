from itertools import permutations

table = '123 2145 316 427 5267 6357 7456'
graph = 'AEDF BFD CFG DBAE EGDA FCBA GCE'

print(*'1234567')
graph_dict = {x[0]: set(x[1:]) for x in graph.split()}
for per in permutations('ABCDEFG'):
    new_graph = table
    for x, y in zip('1234567', per):
        new_graph = new_graph.replace(x, y)
    new_graph = {x[0]: set(x[1:]) for x in new_graph.split()}
    if new_graph == graph_dict:
        print(*per)
