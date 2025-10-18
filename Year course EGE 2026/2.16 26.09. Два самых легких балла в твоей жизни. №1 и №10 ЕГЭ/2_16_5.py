from itertools import permutations

table = '1457 2567 345 4136 5123 6247 7126'
graph = 'AFDB BACG CEDB DCFA EFCG FEDA GEB'

print(*'1234567')
graph = {x[0]: set(x[1:]) for x in graph.split()}
for per in permutations('ABCDEFG'):
    new_graph = table
    for x,y in zip('1234567', per):
        new_graph =new_graph.replace(x,y)
    new_graph = {x[0]: set(x[1:]) for x in new_graph.split()}
    if new_graph == graph:
        print(*per)
