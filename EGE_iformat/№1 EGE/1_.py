from itertools import permutations

table = '13 16 25 26 27 31 34 43 46 47 52 57 61 62 64 72 74 75'
graph = 'GC CG CA AC AE EA EF FE FB BF BD DB DG GD DC CD AB BA'
print('1 2 3 4 5 6 7')
graph_set = set(graph.split())
for per in permutations('ABCDEFG'):
    new_graph = table
    print(per)
    for i in range(7):
        new_graph = new_graph.replace(str(i + 1), per[i])
    if graph_set == set(new_graph.split()):
        print(*per)

