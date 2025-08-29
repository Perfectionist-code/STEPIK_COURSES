from itertools import permutations

table = '12346 216 31678 417 568 61235 734 835'
graph = 'ABC BACDE CABEF DBG EBCHG FCH GED HEF'

print(*'12345678')
graph_dict = {x[0]: set(x[1:]) for x in graph.split()}
for per in permutations('ABCDEFGH'):
    new_graph = table
    for x, y in zip('12345678', per):
        new_graph = new_graph.replace(x, y)
    new_graph = {x[0]: set(x[1:]) for x in new_graph.split()}
    if new_graph == graph_dict:
        print(*per)


