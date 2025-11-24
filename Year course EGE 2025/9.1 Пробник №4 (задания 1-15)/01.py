from itertools import permutations

table = '1237 2167 3156 4567 534 6234 7124'
graph = 'ABCG BACD CABE DBEF ECDG FDG GAFE'

print(*'1234567')
graph = {x[0]: set(x[1:]) for x in graph.split()}

for per in permutations('ABCDEFG'):
    new_graph = table
    for x, y in zip('1234567', per):
        new_graph = new_graph.replace(x, y)
    new_graph = {x[0]: set(x[1:]) for x in new_graph.split()}
    if new_graph == graph:
        print(*per)
