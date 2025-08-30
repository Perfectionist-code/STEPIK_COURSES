from itertools import permutations

table = '1347 2356 3124567 413 523 6237 7136'
graph = 'АБВГ БАГЕ ВАГ ГВАБЕДЖ ДЕЖГ ЕБДГ ЖГД'

print(*'1234567')
graph_dict ={x[0]: set(x[1:]) for x in graph.split()}
for per in permutations('АБВГДЕЖ'):
    new_graph = table
    for x, y in zip('1234567', per):
        new_graph = new_graph.replace(x, y)
    new_graph = {x[0]: set(x[1:]) for x in new_graph.split()}
    if new_graph.__eq__(graph_dict):
        print(*per)


