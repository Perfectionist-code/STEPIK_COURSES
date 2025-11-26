from itertools import permutations

table = '12357 2167 3145 4357 513467 6257 712456'
graph = 'AKQCBR BKPRAC CQAB QKAC RPAB PRKB KQAPB'

print(*'12345678')
graph = {x[0]: set(x[1:]) for x in graph.split()}

for per in permutations('ABCRPKQ'):
    new_graph = table
    for x, y in zip('1234567', per):
        new_graph = new_graph.replace(x, y)
    new_graph = {x[0]: set(x[1:]) for x in new_graph.split()}
    if new_graph == graph:
        print(*per)
