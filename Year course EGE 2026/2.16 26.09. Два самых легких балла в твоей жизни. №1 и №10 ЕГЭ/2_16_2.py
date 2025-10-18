from itertools import permutations

table = '1234567 217 3157 4156 5134 614 7123'
graph = 'ACG BCD CAGFEDB DECB EDCF FECG GACF'

print(*'1234567')
graph_dict = {x[0]: set(x[1:]) for x in graph.split()}

for per in permutations('ABCDEFG'):
    new_graph = table
    for x, y in zip('1234567', per):
        new_graph = new_graph.replace(x, y)
    new_graph = {x[0]: set(x[1:]) for x in new_graph.split()}
    if new_graph == graph_dict:
        print(*per)
