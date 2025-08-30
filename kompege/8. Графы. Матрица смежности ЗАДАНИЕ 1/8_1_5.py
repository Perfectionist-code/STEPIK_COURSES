from itertools import permutations

table = '123567 2145 3146 423 5127 6137 7156'
graph = 'AEBD BADC CBDF DEABCF EGDA FGDC GEF'
graph_dict = {x[0]: set(x[1:]) for x in graph.split()}

print(*'1234567')
for per in permutations('ABCDEFG'):
    new_graph = table
    for x, y in zip('1234567', per):
        new_graph = new_graph.replace(x, y)
    new_graph = {x[0]: set(x[1:]) for x in new_graph.split()}
    if new_graph == graph_dict:
        print(*per)


