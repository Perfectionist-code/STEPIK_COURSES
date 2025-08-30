from itertools import permutations

table = '15 16 24 26 27 28 34 36 37 38 42 43 45 47 51 54 61 62 63 68 72 73 74 78 82 83 86 87'
graph = 'BC CB BA AB CF FC FH HF FE EF FD DF EH HE ED DE EG GE HA AH HG GH GD DG DA AD AG GA'

graph_set = set(graph.split())
print(*'12345678')
for per in permutations('ABCDEFGH'):
    new_graph = table
    for i in range(8):
        new_graph = new_graph.replace(str(i + 1), per[i])
    if set(new_graph.split()) == graph_set:
        print(*per)
