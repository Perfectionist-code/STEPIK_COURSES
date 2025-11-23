from itertools import permutations

table = '13457 2456 3167 4128 5126 62358 7138 8467'
graph = 'ALCQ BKCP CBRAQ QACP RLKC KLRB LKRAP PLQB'

print(*'12345678')
graph = {x[0]: set(x[1:]) for x in graph.split()}

for per in permutations('ABCQRKLP'):
    new_graph = table
    for x,y in zip('12345678', per):
        new_graph =new_graph.replace(x,y)
    new_graph = {x[0]: set(x[1:]) for x in new_graph.split()}
    if new_graph == graph:
        print(*per)