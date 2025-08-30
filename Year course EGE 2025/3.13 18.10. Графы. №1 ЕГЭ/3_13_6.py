from itertools import permutations

table = '1235 214 31456 4236 51367 63457 756'
graph = 'КРП РКТС ПКТЛ ТРПСЛ СРТЛМ ЛПТСМ МСЛ'
print(*'1234567')
graph_dict = {x[0]: set(x[1:]) for x in graph.split()}
for per in permutations('КРПТСЛМ'):
    new_graph = table
    for x, y in zip('1234567', per):
        new_graph = new_graph.replace(x, y)
    new_graph = {x[0]: set(x[1:]) for x in new_graph.split()}
    if new_graph.__eq__(graph_dict):
        print(*per)
