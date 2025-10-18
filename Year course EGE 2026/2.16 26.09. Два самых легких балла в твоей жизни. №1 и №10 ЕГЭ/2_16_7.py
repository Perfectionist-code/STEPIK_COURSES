from itertools import permutations

table = '1568 236 3247 4368 5178 6124 735 8145'
graph = 'АБГЖ БЕГА ВЕГД ГВБА ДКВЖ ЕБКВ ЖАД КЕД'

print(*'12345678')
graph = {x[0]: set(x[1:]) for x in graph.split()}
for per in permutations('АБВГДЕЖК'):
    new_graph = table
    for x, y in zip('12345678', per):
        new_graph = new_graph.replace(x, y)
    new_graph = {x[0]: set(x[1:]) for x in new_graph.split()}
    if graph == new_graph:
        print(*per)