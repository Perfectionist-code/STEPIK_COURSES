from itertools import permutations

table = '167 2356 3247 435 5246 6125 713'
graph = 'ACE BGD CGFA DBE EDFA FGCE GBCF'
graph = {x[0]: set(x[1:]) for x in graph.split()}

print(*'1234567')
for per in permutations('ABCDEFG'):
    new_graph = table
    for x, y in zip('1234567', per):
        new_graph = new_graph.replace(x, y)
    new_graph = {x[0]: set(x[1:]) for x in new_graph.split()}
    if graph == new_graph:
        print(*per)
# Ответ 105

