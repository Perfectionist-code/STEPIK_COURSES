from itertools import permutations

table = '167 2567 3456 435 5234 6123 712'
graph = 'АБВ БАВГ ВАБД ГБДЕ ДВГЗ ЕГЗ ЗДЕ'

print(*'1234567')
graph_dict = {x[0]: set(x[1:]) for x in graph.split()}
for per in permutations('АБВГДЕЗ'):
    new_graph = table
    for x, y in zip('1234567', per):
        new_graph = new_graph.replace(x, y)
    new_graph = {x[0]: set(x[1:]) for x in new_graph.split()}
    if new_graph.__eq__(graph_dict):
        print(*per)


