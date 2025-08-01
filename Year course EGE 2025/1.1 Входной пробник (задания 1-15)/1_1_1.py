from itertools import permutations

table = '14 17 23 24 25 26 32 35 41 42 47 52 53 62 67 71 74 76'
graph = 'AB BA AE EA BE EB EF FE BD DB DF FD FC CF CG GC FG GF'
print('1 2 3 4 5 6 7')
graph_set = set(graph.split())
for per in permutations('ABCDEFG'):
    new_graph = table
    # print(per)
    for i in range(7):
        new_graph = new_graph.replace(str(i + 1), per[i])
    if graph_set == set(new_graph.split()):
        print(*per)

