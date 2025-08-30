from itertools import permutations

table = '2 1367 25 57 347 2 245'
graph = 'В В БЕАК ВГ АДК ГК ВГД'

print(*'1234567')
graph_set = {frozenset(x) for x in graph.split()}
for per in permutations('АБВГДЕК'):
    new_graph = table
    for x, y in zip('1234567', per):
        new_graph = new_graph.replace(x, y)
    new_graph = {frozenset(x) for x in new_graph.split()}
    if new_graph.__eq__(graph_set):
        print(*per)
