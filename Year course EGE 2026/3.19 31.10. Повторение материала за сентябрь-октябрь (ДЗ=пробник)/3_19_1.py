from itertools import permutations

table = '1258 214 367 428 516 6357 7368 8147'
graph = 'AHG BDH CEG DBF EFGC FDHE GAEC HBAF'
graph = {x[0]: set(x[1:]) for x in graph.split()}

print(*'12345678')
for per in permutations('ABCDEFGH'):
    new_graph = table
    for x,y in zip('12345678', per):
        new_graph = new_graph.replace(x, y)
    new_graph = {x[0]: set(x[1:]) for x in new_graph.split()}
    if new_graph == graph:
        print(*per)