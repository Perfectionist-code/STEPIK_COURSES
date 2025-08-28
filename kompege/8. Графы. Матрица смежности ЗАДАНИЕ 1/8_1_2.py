from itertools import permutations

table = '156 247 346 4236 516 613457 726'
greph = 'АБВ БАВ ВАБДГК ГВК ДВЕ ЕДК КВЕГ'

print(*'1234567')
greph_dict = {x[0]: set(x[1:]) for x in greph.split()}
for per in permutations('АБВГДЕК'):
    new_graph = table
    for x, y in zip('1234567', per):
        new_graph = new_graph.replace(x, y)
    new_graph = {x[0]: set(x[1:]) for x in new_graph.split()}
    if new_graph == greph_dict:
        print(*per)


